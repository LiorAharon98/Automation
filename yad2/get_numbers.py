from selenium.webdriver.common.by import By
import time
from config_driver import driver
from city_class import city
from create_txt_file import create_txt


def getNumbers():

    numbers = []

    for page_index in range(1, 3):
        driver.get(
            f'https://www.yad2.co.il/realestate/{city.rent_or_forsale}?topArea={city.top_area}&area={city.area}&city={city.city}&neighborhood={city.neighborhood}&page={page_index}')
        is_relator_post_cnt = driver.find_elements(
            By.CSS_SELECTOR, ".feed_item-v4.accordion.agency.platinum.desktop").__len__()
        groups = driver.find_elements(By.CSS_SELECTOR, ".feeditem.table")
        for i in range(0, groups.__len__()):
            try:
                time.sleep(1)
                if groups[i].find_elements(By.CSS_SELECTOR, ".ribbon.bg_pumpkin_orange").__len__() != 0:
                    continue
                if groups[i].find_elements(By.CSS_SELECTOR, ".feed_item.feed_item-v4.accordion.agency.desktop").__len__() != 0:
                    break

                groups[i].click()
                time.sleep(2)
                contact_seller_btn = driver.find_element(
                    By.CLASS_NAME, "contact-seller-btn")
                contact_seller_btn.click()

                time.sleep(3)
                phoneNumber = driver.find_element(
                    By.ID, 'phone_number_{}'.format(i+is_relator_post_cnt))
                numbers.append(phoneNumber.text)
                groups[i].find_element(
                    By.CSS_SELECTOR, ".color_container").click()

            except Exception as error:
                create_txt(city.name, numbers, error)
    create_txt(city.name, numbers, False)


getNumbers()
while (True):
    pass
