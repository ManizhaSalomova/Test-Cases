import email
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def clickHelp():
    # Declairing variables
    url = "https://www.hudl.com/login"

    # Access to URL and test with invalid input
    driver.get(url)
    time.sleep(1)

    # Click Sign up link
    driver.find_element_by_link_text("Sign up").click()

    # Assert that "Login Help" is visible
    assert(len(driver.find_elements_by_xpath(
        "//h1[text() = 'Request a Free Demo']"))) > 0
    print('Log in" page - working as expected')


driver = webdriver.Chrome(ChromeDriverManager().install())
clickHelp()
