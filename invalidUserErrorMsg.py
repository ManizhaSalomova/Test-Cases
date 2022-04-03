from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Validating Error message when email is invalid


class InvalidUserLoginError:
    # Declairing variables
    url = "https://www.hudl.com/login"
    invalid_email = 'jjjj@gmail.com'
    invalid_password = 'hello'
    expected_msg = "We didn't recognize that email and/or password. Need help?"

    # define the browser we run the test (Chrome)
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(3)
        time.sleep(2)

    def go_to_myaccount(self):
        self.driver.get(self.url)
        time.sleep(2)

    def input_email(self):
        field = self.driver.find_element_by_id('email')
        field.send_keys(self.invalid_email)
        time.sleep(2)

    def input_password(self):
        field = self.driver.find_element_by_id('password')
        field.send_keys(self.invalid_password)
        time.sleep(2)

    def click_login(self):
        self.driver.find_element_by_id('logIn').click()
        time.sleep(2)

    def verify_error_message(self):
        err_elm = self.driver.find_element_by_xpath(
            "/html/body/div[2]/form[1]/div[3]/div/p")
        display_err = err_elm.text
        assert display_err == self.expected_msg, "The display error is not expected"
        print('PASS')
        time.sleep(4)

    def main(self):
        self.go_to_myaccount()
        self.input_email()
        self.input_password()
        self.click_login()
        self.verify_error_message()
        self.driver.quit()


if __name__ == '__main__':

    obj = InvalidUserLoginError()
    # calling above methods
    obj.main()
