from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def login():
    # Declairing variables
    url = 'https://www.hudl.com/login'

    # Access to URL and test with invalid input
    driver.get(url)
    time.sleep(1)
    get_title = driver.title
    print(get_title)
    time.sleep(2)
    assert 'Log In - Hudl' in driver.title, 'Wrong title displayed'
    time.sleep(3)

driver = webdriver.Chrome(ChromeDriverManager().install())
login()
