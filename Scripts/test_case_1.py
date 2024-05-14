import time

from webdriverInitializer import initialize_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def NavigateToAutomationPage():
    driver = initialize_driver()
    driver.implicitly_wait(10)

    driver.maximize_window()
    driver.get('https://www.sogeti.com')
    driver.find_element(By.XPATH, '//button[contains(text(),"Allow all cookies")]').click()

    elementToHoverOver = driver.find_element(By.XPATH,'(//span[contains(text(), "Services")]//parent::div//parent::li)[1]')
    hover = ActionChains(driver).move_to_element(elementToHoverOver)
    hover.perform()

    automationButton = driver.find_element(By.XPATH,'(//span[contains(text(), "Services")]//parent::div//child::ul//child::li//child::a[contains(text(), "Automation")])[1]')
    automationButton.click()

    automationLi = driver.find_element(By.XPATH, '(//span[contains(text(), "Services")]//parent::div//child::ul//child::li//child::a[contains(text(), "Automation")]//parent::li)[1]')
    class_name = automationLi.get_attribute("class")

    if class_name == "selected  current expanded":
        print('Automation page is being displayed!')
    else:
        print('Automation page is not being displayed!')

    time.sleep(2)
    driver.quit()

if __name__ == '__main__':
    NavigateToAutomationPage()