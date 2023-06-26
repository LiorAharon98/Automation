import undetected_chromedriver as uc
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = uc.Chrome()
driver.maximize_window()


def handleTool():
    driver.get("https://www.madlan.co.il/personal/login")
    time.sleep(1)
    botDetection = driver.find_elements(
        By.XPATH, "/html/body/section[2]/div[1]/h1")
    if botDetection.__len__() != 0:
        return

    time.sleep(1)
    driver.find_element(By.NAME, "email").send_keys(
        'orna.realestate@gmail.com')
    time.sleep(1)
    driver.find_element(By.NAME, "password").send_keys('orna1964', Keys.RETURN)
    time.sleep(1.5)
    driver.find_elements(By.CSS_SELECTOR, ".btn-block.btn.btn-info")[0].click()
    time.sleep(1)
    groupPosts = driver.find_elements(
        By.CSS_SELECTOR, ".fa.fa-pencil").__len__()
    for index in range(1, groupPosts+1):
        driver.find_element(
            By.XPATH, "/html/body/div[4]/div[2]/section[2]/div/div[9]/div/div/div/div/div[2]/table/tbody/tr[{}]/td[13]/a".format(index)).click()
        time.sleep(1)
        driver.find_element(
            By.CSS_SELECTOR, ".refreshBulletin.btn.btn-link").click()
        time.sleep(1)
        driver.switch_to.alert.accept()
        driver.back()
        time.sleep(1)


handleTool()
while (True):
    pass
