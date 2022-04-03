import email
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class BackToLogIng:
    # Declairing variables
    url = "https://www.hudl.com/login"

    # Click on "Sign Up" validate the page, then click back to "log In" Page.
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(3)
        time.sleep(2)

    def go_to_myaccount(self):
        self.driver.get(self.url)
        time.sleep(1)

    def click_sign_up(self):
        self.driver.find_element_by_link_text("Sign up").click()
        time.sleep(1)

    # click on "Log in"
    def click_log_in(self):
        self.driver.find_element_by_link_text("Log in").click()
        time.sleep(1)

    def validate_log_in(self):
        # Assert that "Login Help" is visible
        assert(len(self.driver.find_elements_by_xpath(
            "/html/body/div[2]/form[1]/div[1]/a"))) > 0
        print('Log in" validated')

    def main(self):
        self.go_to_myaccount()
        self.click_sign_up()
        self.click_log_in()
        self.validate_log_in()
        self.driver.quit()


if __name__ == '__main__':

    obj = BackToLogIng()
    # calling above methods
    obj.main()
