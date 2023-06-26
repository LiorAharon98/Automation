from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc
chrome_options = Options()
chrome_options.add_argument(
    "--load-extension=" + 'C:\\Users\\Lior\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Extensions\\cjpalhdlnbpafiamejdnhcphjbkeiagm\\1.50.0_0')
driver = uc.Chrome(chrome_options)
driver.maximize_window()
