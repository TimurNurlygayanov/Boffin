# Copyright (c) 2013 Mirantis Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import boffin.page as page


class DemoPage(page.Page):
    """
        This class it is a simple page object.
        Each page object must inherit from page.Page class.
    """

    name = 'Demo'

    def search(self, text):
        page = self.page
        text = 'Boffin framework'
        page.EditBox('String For Search').Set(text)
        page.Button('Search').Click()