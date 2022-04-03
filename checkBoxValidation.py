from lib2to3.pgen2 import driver
from xml.dom.minidom import Element
from xml.sax.xmlreader import Locator
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


class Checkboxe:
    # Declairing variables
    url = "https://www.hudl.com/login"

    # define the browser we run the test (Chrome)
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(3)
        time.sleep(2)

    def go_to_myaccount(self):
        self.driver.get(self.url)
        time.sleep(2)

    # is checkbox selected?
    def checkbox(self):
        element = self.driver.find_element_by_id('remember-me')
        element2 = self.driver.find_element_by_class_name("checkbox-container")
        element2.click()
        time.sleep(1)
        assert element.is_selected(),  "element is not selected"
        # print(element.is_selected())
        time.sleep(5)

    def main(self):
        self.go_to_myaccount()
        self.checkbox()
        self.driver.quit()


if __name__ == '__main__':

    obj = Checkboxe()
    # calling above methods
    obj.main()
