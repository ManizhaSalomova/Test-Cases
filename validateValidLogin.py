from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


class InvalidUserLoginError:
    # Declairing variable
    url = "https://www.hudl.com/login"
    username = 'jingonya@yahoo.com'
    password = 'Madina0909$'

    # define the browser we run the test (Chrome)
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(3)
        time.sleep(2)

    def go_to_myaccount(self):
        self.driver.get(self.url)
        time.sleep(1)

    def input_email(self):
        field = self.driver.find_element_by_id('email')
        field.send_keys(self.username)
        time.sleep(1)

    def input_password(self):
        field = self.driver.find_element_by_id('password')
        field.send_keys(self.password)
        time.sleep(1)

    def click_login(self):
        self.driver.find_element_by_id('logIn').click()
        time.sleep(1)

    def validate_login(self):
        # Assert that "Profile/Home  Page" is visible
        assert self.driver.find_element_by_xpath(
            '//*[@id="ssr-webnav"]/div/div[1]/nav[1]/div[4]/div[2]/div[1]/div[1]/div/div').is_displayed() == True
        time.sleep(3)

    def main(self):
        self.go_to_myaccount()
        self.input_email()
        self.input_password()
        self.click_login()
        self.validate_login()
        self.driver.quit()


if __name__ == '__main__':

    obj = InvalidUserLoginError()
    # calling above methods
    obj.main()
