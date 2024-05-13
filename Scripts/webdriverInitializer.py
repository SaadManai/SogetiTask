from selenium import webdriver

def initialize_driver():
    # Initialize the WebDriver (Chrome in this example)
    driver = webdriver.Chrome()
    return driver
