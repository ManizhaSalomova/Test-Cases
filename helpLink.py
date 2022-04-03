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

    # Click help link
    driver.find_element_by_id("forgot-password-link").click()

    # Assert that "Login Help" is visible
    assert(len(driver.find_elements_by_xpath(
        "//h1[text() = 'Login Help']"))) > 0
    print('Need help" - working as expected - redirecting to the resset password pageclear')


driver = webdriver.Chrome(ChromeDriverManager().install())
clickHelp()
