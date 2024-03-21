# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import hashlib
import os
import typing

from docutils import nodes
from docutils.parsers.rst import directives
from docutils.statemachine import ViewList
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from playwright.sync_api import sync_playwright
from sphinx.application import Sphinx
from sphinx.util.docutils import SphinxDirective

Meta = typing.TypedDict('Meta', {
    'version': str,
    'parallel_read_safe': bool,
    'parallel_write_safe': bool
})

p = sync_playwright().start()
browser = p.chromium.launch()


class ScreenshotDirective(SphinxDirective):
  """Sphinx Screenshot Dirctive.

  This directive embeds a screenshot of a webpage.

  # Example

  You can simply pass a URL for a webpage that you want to take a screenshot.

  ```rst
  .. screenshot:: http://www.example.com
  ```

  You can also specify the screen size for the screenshot with `width` and
  `height` parameters in pixel.

  ```rst
  .. screenshot:: http://www.example.com
    :width: 1280
    :height: 960
  ```

  You can include a caption for the screenshot's `figure` directive.

  ```rst
  .. screenshot:: http://www.example.com
    :caption: This is a screenshot for www.example.com
  ```

  You can describe the interaction that you want to have with the webpage
  before taking a screenshot. `page` is the
  [Playwright's Page instance](https://playwright.dev/docs/api/class-page).

  ```rst
  .. screenshot:: http://www.example.com

      page.get_by_role('link').click()
  ```

  You can even specify the webpage with a file path.
  If it's a relative path, the origin should be the document source directory.

  ```rst
  .. screenshot:: ./example.html
  ```
  """

  required_arguments = 1  # URL
  has_content = True
  option_spec = {
      'height': directives.positive_int,
      'width': directives.positive_int,
      'caption': directives.unchanged,
  }

  def run(self) -> typing.List[nodes.Node]:
    screenshot_init_script = self.env.config.screenshot_init_script

    # Ensure the screenshots directory exists
    ss_dirpath = os.path.join(self.env.app.outdir, '_static', 'screenshots')
    os.makedirs(ss_dirpath, exist_ok=True)

    # Parse parameters
    url_or_path = self.arguments[0]
    height = self.options.get('height', 960)
    width = self.options.get('width', 1280)
    caption_text = self.options.get('caption', '')
    interactions = '\n'.join(self.content)

    # Generate filename based on hash of parameters
    hash_input = f'{url_or_path}_{height}_{width}_{interactions}'
    filename = hashlib.md5(hash_input.encode()).hexdigest() + '.png'
    filepath = os.path.join(ss_dirpath, filename)

    # Check if the file already exists. If not, take a screenshot
    if not os.path.exists(filepath):
      page = browser.new_page()
      page.set_default_timeout(10000)
      page.set_viewport_size({'width': width, 'height': height})
      try:
        if screenshot_init_script:
          page.add_init_script(screenshot_init_script)
        if url_or_path.startswith(('http://', 'https://')):
          page.goto(url_or_path)
        elif os.path.isabs(url_or_path):
          page.goto('file://' + url_or_path)
        else:
          page.goto('file://' + str(self.env.srcdir.joinpath(url_or_path)))
        page.wait_for_load_state('networkidle')

        # Execute interactions
        if interactions:
          exec(interactions)
      except PlaywrightTimeoutError:
        raise RuntimeError('Timeout error occured at %s in executing\n%s' %
                           (url_or_path, interactions))

      page.screenshot(path=filepath)
      page.close()

    # Create image and figure nodes
    docdir = os.path.dirname(self.env.doc2path(self.env.docname))
    rel_ss_dirpath = os.path.relpath(ss_dirpath, start=docdir)
    rel_filepath = os.path.join(rel_ss_dirpath, filename).replace(os.sep, '/')
    image_node = nodes.image(uri=rel_filepath)
    figure_node = nodes.figure('', image_node)

    if caption_text:
      parsed = nodes.Element()
      self.state.nested_parse(
          ViewList([caption_text], source=''), self.content_offset, parsed)
      figure_node += nodes.caption(parsed[0].source or '', '',
                                   *parsed[0].children)

    return [figure_node]


def on_build_finished(app: Sphinx, exception: Exception):
  browser.close()
  p.stop()


def setup(app: Sphinx) -> Meta:
  app.add_directive('screenshot', ScreenshotDirective)
  app.connect('build-finished', on_build_finished)
  app.add_config_value('screenshot_init_script', '', 'env')
  return {
      'version': '0.0.3',
      'parallel_read_safe': True,
      'parallel_write_safe': True,
  }
