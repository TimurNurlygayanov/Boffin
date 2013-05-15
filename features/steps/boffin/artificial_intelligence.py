from bs4 import BeautifulSoup


class ArtificialIntelligence:
    """
        This class allows to find input and select controls
        without manual input of identificators.
        We can find input fields by labels near those fields
    """

    def __init__(self, driver):
        self.driver = driver

    def _get_xpath_of_element(self, element):
        " this funcion allows to get xpath of soup elements "

        xpath = element.name

        for parent in element.findParents():
            if parent.name != '[document]':
                k = 0
                for tag in parent.find_previous_siblings():
                    if tag.name == parent.name:
                        k += 1
                if k == 0:
                    xpath = parent.name + '/' + xpath
                else:
                    xpath = parent.name + '[' + str(k+1) + ']/' + xpath

        xpath = '/html/body/' + xpath
        return xpath

    def find_element(self, label, element_type='input'):
        element = None

        " get html code of page "
        page = self.driver.find_element_by_tag_name("body")
        html = page.get_attribute("innerHTML")
        html = str(html.encode("utf-8", "replace"))

        " load html to soup structure for parsing "
        soup = BeautifulSoup(html)

        " search label in html code "
        label_element = soup.find(text=str(label))

        " search input element after the label"
        input_element = label_element.parent.find_next(element_type)

        " return xpath of input element "
        xpath = self._get_xpath_of_element(input_element)
        element = driver.find_element_by_xpath(xpath)
        return element
