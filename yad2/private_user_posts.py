def private_user(driver, By):
    multiplePosts = driver.find_elements(
        By.CLASS_NAME, "ad_mainContainer__boaaB")
    for i in range(0, multiplePosts.__len__()):
        driver.find_element(
            By.XPATH,
            f'/html/body/div[2]/div/main/div[2]/div[{i + 2}]/div/div[2]/div/div[1]/div[2]/div/div/div[3]/button[2]'

        ).click()
        private_user()
