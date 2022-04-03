import email
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Access "Need help?" to validate "forgot-password-link" - email was sent


class needHelpPage:
    # Declairing variables
    url = "https://www.hudl.com/login"
    invalid_email = 'sample@gmail.com'
    expected_msg = "Check Your Email"

    # define the browser we run the test (Chrome)
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(3)
        time.sleep(2)

    def needHelp(self):
        # Access to URL and test with invalid input
        self.driver.get(self.url)
        time.sleep(1)

        # Click help link
        self.driver.find_element_by_id("forgot-password-link").click()

    def input_email(self):
        field = self.driver.find_element_by_id('forgot-email')
        field.send_keys(self.invalid_email)
        time.sleep(1)

    def send_password_reset(self):
        self.driver.find_element_by_id('resetBtn').click()
        time.sleep(1)
    # if email address missing @ sign should get the error message

    def verify_error_msg(self):
        # Enter valid email to reset password
        err_msg = self.driver.find_element_by_xpath(
            "//h4[text() = 'Check Your Email']")
        display_err = err_msg.text
        assert display_err == self.expected_msg, "The display error message is not the same."
        print('PASS')

    def main(self):
        self.needHelp()
        self.input_email()
        self.send_password_reset()
        self.verify_error_msg()
        self.driver.quit()


if __name__ == '__main__':

    obj = needHelpPage()
    # calling above methods
    obj.main()
