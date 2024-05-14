import time
import string
import random
import secrets

from webdriverInitializer import initialize_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def SubmitContactForm():
    driver = initialize_driver()
    driver.implicitly_wait(10)

    driver.maximize_window()
    driver.get('https://www.sogeti.com')
    driver.find_element(By.XPATH, '//button[contains(text(),"Allow all cookies")]').click()

    # get the xpath of the element to hover on
    element = driver.find_element(By.XPATH,'(//span[contains(text(), "Services")]//parent::div//parent::li)[1]')
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()

    automationButton = driver.find_element(By.XPATH,'(//span[contains(text(), "Services")]//parent::div//child::ul//child::li//child::a[contains(text(), "Automation")])[1]')
    automationButton.click()

    firstName = driver.find_element(By.XPATH, '//label[contains(text(), "First Name")]//following-sibling::input')
    enterText(firstName, driver)

    lastName = driver.find_element(By.XPATH, '//label[contains(text(), "Last Name")]//following-sibling::input')
    enterText(lastName, driver)

    email = driver.find_element(By.XPATH, '//label[contains(text(), "Email")]//following-sibling::input')
    email.send_keys(f"{secrets.token_hex(8)}@gmail.com")

    phone = driver.find_element(By.XPATH, '//label[contains(text(), "Phone")]//following-sibling::input')
    phone.send_keys(generatePhoneNumber())

    company = driver.find_element(By.XPATH, '//label[contains(text(), "Company")]//following-sibling::input')
    enterText(company, driver)

    countrySelect = driver.find_element(By.XPATH, '//label[contains(text(), "Country")]//following-sibling::div//child::select')
    time.sleep(4)
    driver.execute_script("arguments[0].scrollIntoView();", phone)
    countrySelect.click()
    time.sleep(1)
    countryOptions = driver.find_elements(By.XPATH, '//option')
    selectedCountry = random.randint(0, len(countryOptions))
    countryOptions[selectedCountry].click()

    message = driver.find_element(By.XPATH, '//label[contains(text(), "Message")]//following-sibling::textarea')
    enterText(message, driver)

    checkbox = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@id='__field_1239350']")))
    driver.execute_script("arguments[0].click();", checkbox)

    try:
        # Wait until the iframe containing the checkbox is present
        iframe = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//iframe[contains(@title, 'reCAPTCHA')]"))
        )

        # Switch to the iframe
        driver.switch_to.frame(iframe)

        # Locate the checkbox element using XPath
        checkbox_xpath = '//div[@class="recaptcha-checkbox-border"]'
        checkbox = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, checkbox_xpath))
        )

        # Click the checkbox
        checkbox.click()

        # Switch back to the main content
        driver.switch_to.default_content()

    finally:
        time.sleep(2)
        driver.quit()

def enterText(ele, driver):
    driver.execute_script("arguments[0].scrollIntoView();", ele)
    # generating random strings
    text = ''.join(random.choices(string.ascii_uppercase +
                                 string.digits, k=7))
    ele.send_keys(str(text))

def generatePhoneNumber():
    digits = [5, 6, 8, 0, 3, 4]
    number = '0176'

    for _ in range(6):
        digit = random.choice(digits)
        number += str(digit)

    return number

if __name__ == '__main__':
    SubmitContactForm()