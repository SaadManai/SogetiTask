import time
import re

from webdriverInitializer import initialize_driver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

def VerifyAllLocationsPage():
    driver = initialize_driver()
    driver.implicitly_wait(10)

    driver.maximize_window()
    driver.get('https://www.sogeti.com')
    driver.find_element(By.XPATH, '//button[contains(text(),"Allow all cookies")]').click()

    driver.find_element(By.XPATH, '//div[@aria-controls="country-list-id"]').click()
    time.sleep(1)

    countryLinks = driver.find_elements(By.XPATH, '//div[@id="country-list-id"]//child::ul//child::li//child::a')
    print(countryLinks)
    for link in countryLinks:
        link.click()
        time.sleep(2)
        src = driver.page_source
        if re.search(r'Sogeti', src):
            print('Page is running!')
        else:
            print('Page is not running!')

        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + 't')
        driver.switch_to.window(driver.window_handles[1])
        driver.get("https://www.sogeti.com")
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

    time.sleep(2)
    driver.quit()

if __name__ == '__main__':
    VerifyAllLocationsPage()