from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc
driver = uc.Chrome()
def search():
    try:
       driver.get("https://www.komo.co.il/code/nadlan/apartments-for-sale.asp?nehes=1&cityName=%D7%91%D7%90%D7%A8+%D7%A9%D7%91%D7%A2")
    except Exception as e:
        print(e)

    search()