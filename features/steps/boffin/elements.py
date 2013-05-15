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

import logging
from selenium.webdriver.support.ui import Select

logging.basicConfig()
LOG = logging.getLogger('elements')


class Object:
    obj = None
    browser = None

    def __init__(self, obj, browser):
        self.browser = browser
        if not obj:
            LOG.error('Object does not found')
        self.obj = obj

    def isPresented(self):
        if self.obj:
            return True
        return False

    def Text(self):
        if self.obj:
            text = self.obj.get_text()
            self.browser.page.switch_to_default_content()
            return text
        else:
            return ''

    def Click(self):
        if self.obj:
            self.obj.click()
        self.browser.page.switch_to_default_content()


class TableCellClass(Object):
    pass


class Label(Object):
    pass


class ButtonClass(Object):
    pass


class LinkClass(Object):

    def Address(self):
        if self.obj:
            link = self.obj.get_attribute('href')
            self.browser.page.switch_to_default_content()
            return link
        else:
            return ''


class EditBoxClass(Object):

    def Set(self, value):
        if self.obj:
            try:
                self.obj.clear()
                self.obj.send_keys(value)
            except:
                LOG.error('Can not set value for text box.')
        self.browser.page.switch_to_default_content()


class DropDownListClass(Object):

    def Set(self, value):
        if self.obj:
            try:
                Select(self.obj).select_by_visible_text(value)
            except:
                message = "Can not select element %s from drop down list."
                LOG.error(message % value)
        self.browser.page.switch_to_default_content()


class CheckBox(Object):

    def isSelected(self):
        if self.obj:
            status = self.obj.is_selected()
            self.browser.page.switch_to_default_content()
            return status

    def Select(self):
        if self.obj:
            if not self.obj.is_selected():
                self.obj.click()
        self.browser.page.switch_to_default_content()

    def Clear(self):
        if self.obj:
            if self.obj.is_selected():
                self.obj.click()
        self.browser.page.switch_to_default_content()


class RadioButton(Object):

    def isSelected(self):
        if self.obj:
            status = self.obj.is_selected()
            self.browser.page.switch_to_default_content()
            return status

    def Select(self):
        if self.obj:
            if not self.obj.is_selected():
                self.obj.click()
        self.browser.page.switch_to_default_content()

    def Clear(self):
        if self.obj:
            if self.obj.is_selected():
                self.obj.click()
        self.browser.page.switch_to_default_content()
