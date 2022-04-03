import email
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def clickLogInOrg():
    # Declairing variables
    url = "https://www.hudl.com/login"

    # Access to URL and test with invalid input
    driver.get(url)
    time.sleep(1)

    # Click help link
    driver.find_element_by_id("logInWithOrganization").click()

    # Assert that "Login Help" is visible
    assert (len(driver.find_elements_by_xpath(
        "//h2[text() = 'Log into Hudl with your Organization']"))) > 0
    print("PASS")
    time.sleep(3)


driver = webdriver.Chrome(ChromeDriverManager().install())
clickLogInOrg()
driver.quit()
