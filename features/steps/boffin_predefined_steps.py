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


from selenium import webdriver
from behave import *


def check(browser, condition):
    if condition:
        browser.logger.test_case_finish()
    else:
        screenshot = browser.driver.get_screenshot_as_base64()
        browser.dblogger.save_screenshot(screenshot)
        browser.dblogger.test_case_finish('FAILED')
    assert condition


@given('browser with new page "{page_url}"')
def step(browser, page_url):
    try:
        browser.driver.close()
        browser.driver = webdriver.Firefox()
        browser.driver.maximize_window()
    except:
        pass

    browser.page.Open(page_url)


@when('I navigate to "{path}"')
def step(browser, path):
    browser.page.Navigate(path)


@when('I move cursor to "{element_name}"')
def step(browser, element_name):
    action = webdriver.common.action_chains.ActionChains(browser.driver)

    element = page.Button(element_name)
    action.move_to_element(element)

    action.perform()


@when('I click on button "{button_name}"')
def step(browser, button_name):
    browser.page.Button(button_name).Click()


@when('I click on link "{link}"')
def step(browser, link):
    browser.page.Link(link).Click()


@when('I set value "{value}" for edit box "{edit_box_name}"')
def step(browser, value, edit_box_name):
    browser.page.EditBox(edit_box_name).Set(value)


@when('I select item "{value}" from drop down list "{list_name}"')
def step(browser, value, list_name):
    browser.page.DropDownList(list_name).Set(value)


@when('I remember text from "{element_name}"')
def step(browser, element_name):
    browser.text_for_check = browser.page.Label(element_name).Text()


@then('text of "{element_name}" is equal to text from memory')
def step(browser, link_text):
    text = browser.page.Label(element_name).Text()
    check(browser, text == browser.text_for_check)


@then('page should contain link "{link_text}"')
def step(browser, link_text):
    check(browser, browser.page.Link(link_text).isPresented())


@then('page should not contain link "{link_text}"')
def step(browser, link_text):
    check(browser, not browser.page.Link(link_text).isPresented())


@then('page should contain button "{button_name}"')
def step(browser, button_name):
    check(browser, browser.page.Button(button_name).isPresented())


@then('page should not contain button "{button_name}"')
def step(browser, button_name):
    check(browser, not browser.page.Button(button_name).isPresented())


@then('text of {cell_name} is equal to "{text}"')
def step(browser, cell_name, text):
    check(browser, browser.page.TableCell(link_text).isPresented())
    check(browser, text in browser.page.TableCell(link_text).Text())


@then('text of {cell_name} is not equal to "{text}"')
def step(browser, cell_name, text):
    check(browser, not text in browser.page.TableCell(link_text).Text())
