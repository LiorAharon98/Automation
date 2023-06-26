from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import undetected_chromedriver as uc
from private_user_posts import private_user


def autoPosts():
    driver = uc.Chrome()
    driver.maximize_window()
    actions = ActionChains(driver)

    try:
        driver.get("https://www.yad2.co.il/auth/login")

        driver.find_element(By.ID, "email").send_keys(
            "lior.ah98@gmail.com")
        driver.find_element(By.ID, "password").send_keys(
            "lior.a98")
        driver.find_element(By.CLASS_NAME, "text").click()
        time.sleep(3)
        ele = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".user-drop-container_userButtonWrapper__u2xAp.user-drop-container_is-inline-for-user-content__yCO1g")))
        actions.move_to_element(ele).perform()
        driver.find_element(
            By.CSS_SELECTOR, ".option_option___Iz7N.option_hoisted__Pp0vT").click()

        time.sleep(2)
        private_user(driver, By)
    except Exception as e:
        print(e)


autoPosts()
while (True):
    pass
