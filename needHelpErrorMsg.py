import email
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Access "Need help?" to validate error msg for invalid email


class needHelpPage:
    # Declairing variables
    url = "https://www.hudl.com/login"
    invalid_email = 'jjjj'
    # change the message below to FAIL the test
    expected_msg = "That isn't a valid email address. Make sure to use the email@domain.com format."

    # define the browser we run the test (Chrome)
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(3)
        time.sleep(2)

    def need_help(self):
        # Access "Need help?" to validate error msg
        self.driver.get(self.url)
        time.sleep(2)

        # Click help link
        self.driver.find_element_by_id("forgot-password-link").click()

    def input_email(self):
        field = self.driver.find_element_by_id('forgot-email')
        field.send_keys(self.invalid_email)
        time.sleep(2)

    def click_log_in(self):
        self.driver.find_element_by_id('resetBtn').click()
        time.sleep(2)

    # if email address missing @ sign should get the error message
    def verify_error_msg(self):
        # Enter valid email to reset password
        err_msg = self.driver.find_element_by_xpath(
            "/html/body/div[2]/form[2]/div[2]/div[2]/div/p")
        display_err = err_msg.text
        assert display_err == self.expected_msg, "The display error message is not the same."
        print('PASS')
        time.sleep(2)

    def main(self):
        self.need_help()
        self.input_email()
        self.click_log_in()
        self.verify_error_msg()

        self.driver.quit()


if __name__ == '__main__':

    obj = needHelpPage()
    # calling above methods
    obj.main()
