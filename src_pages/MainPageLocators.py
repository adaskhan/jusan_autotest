from selenium.webdriver.common.by import By


class ProductSectionLocators:
    ONLINE_CREDIT = (By.XPATH, "/html/body/div/div/section/div/section[1]/div/div[2]/a[1]")
    JUSAN_DEPOSIT = (By.XPATH, "/html/body/div/div/section/div/section[1]/div/div[2]/a[2]")
    CARD_JUSAN = (By.XPATH, "/html/body/div/div/section/div/section[1]/div/div[2]/a[3]")
    CREDIT_REFINANCE = (By.XPATH, "/html/body/div/div/section/div/section[1]/div/div[2]/a[4]")
    MASTERCARD_WORLD_ELITE = (By.XPATH, "/html/body/div/div/section/div/section[1]/div/div[2]/a[5]")


class StoreSectionLocators:
    LAPTOPS_AND_LOCATORS = (By.XPATH, "/html/body/div/div/section/div/section[2]/div/div[2]/a[1]")
    HOME_FURNITURE = (By.XPATH, "/html/body/div/div/section/div/section[2]/div/div[2]/a[2]")
    SMARTPHONES_AND_GADGETS = (By.XPATH, "/html/body/div/div/section/div/section[2]/div/div[2]/a[3]")
    SPORT_AND_TOURISM = (By.XPATH, "/html/body/div/div/section/div/section[2]/div/div[2]/a[4]")
    HOME_APPLIANCES = (By.XPATH, "/html/body/div/div/section/div/section[2]/div/div[2]/a[5]")
    TV_AUDIO_VIDEO_AND_PHOTO = (By.XPATH, "/html/body/div/div/section/div/section[2]/div/div[2]/a[6]")
