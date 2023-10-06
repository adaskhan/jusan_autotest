import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage
from src_pages.MainPageLocators import ProductSectionLocators, StoreSectionLocators
from .express_page import ExpressPage
from .jmart_page import JMart
from .jusan_deposit_page import JusanDepositPage
from .card_jusan_page import CardJusanPage
from .credit_refinance_page import CreditRefinancePage
from .card_mastercard_page import CardMastercardPage


class Products(BasePage):

    def go_to_online_credit_page(self):
        button_online_credit = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(ProductSectionLocators.ONLINE_CREDIT)
        )
        button_online_credit.click()
        return ExpressPage(browser=self.browser, url=self.browser.current_url)

    def go_to_jusan_deposit_page(self):
        button_jusan_deposit = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(ProductSectionLocators.JUSAN_DEPOSIT)
        )
        button_jusan_deposit.click()
        return JusanDepositPage(browser=self.browser, url=self.browser.current_url)

    def go_to_card_jusan_page(self):
        button_card_jusan = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(ProductSectionLocators.CARD_JUSAN)
        )
        button_card_jusan.click()
        return CardJusanPage(browser=self.browser, url=self.browser.current_url)

    def go_to_credit_refinance_page(self):
        self.browser.execute_script(f"window.scrollBy(0, 800);")
        time.sleep(3)
        button_credit_refinance = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(ProductSectionLocators.CREDIT_REFINANCE)
        )
        button_credit_refinance.click()
        return CreditRefinancePage(browser=self.browser, url=self.browser.current_url)

    def go_to_card_mastercard_page(self):
        self.browser.execute_script(f"window.scrollBy(0, 800);")
        time.sleep(3)
        button_card_mastercard = self.browser.find_element(*ProductSectionLocators.MASTERCARD_WORLD_ELITE)
        button_card_mastercard.click()
        return CardMastercardPage(browser=self.browser, url=self.browser.current_url)


class Store(BasePage):

    def go_to_laptops_and_computers_jmart_page(self):
        self.browser.execute_script(f"window.scrollBy(0, 1400);")
        time.sleep(3)
        button_laptops_and_computers = self.browser.find_element(*StoreSectionLocators.LAPTOPS_AND_LOCATORS)
        button_laptops_and_computers.click()
        return JMart(browser=self.browser, url=self.browser.current_url)

    def go_to_home_furniture_jmart_page(self):
        self.browser.execute_script(f"window.scrollBy(0, 1400);")
        time.sleep(3)
        button_home_furniture = self.browser.find_element(*StoreSectionLocators.HOME_FURNITURE)
        button_home_furniture.click()
        return JMart(browser=self.browser, url=self.browser.current_url)

    def go_to_smartphones_and_gadget_jmart_page(self):
        # self.browser.execute_script(f"window.scrollBy(0, 1400);")
        # time.sleep(3)
        button_smartphones_and_gadget = self.browser.find_element(*StoreSectionLocators.SMARTPHONES_AND_GADGETS)
        button_smartphones_and_gadget.click()
        return JMart(browser=self.browser, url=self.browser.current_url)

    def go_to_sport_and_tourism_jmart_page(self):
        # self.browser.execute_script(f"window.scrollBy(0, 1400);")
        # time.sleep(3)
        button_sport_and_tourism = self.browser.find_element(*StoreSectionLocators.SPORT_AND_TOURISM)
        button_sport_and_tourism.click()
        return JMart(browser=self.browser, url=self.browser.current_url)

    def go_to_home_appliances_jmart_page(self):
        # self.browser.execute_script(f"window.scrollBy(0, 1400);")
        # time.sleep(3)
        button_home_appliances = self.browser.find_element(*StoreSectionLocators.HOME_APPLIANCES)
        button_home_appliances.click()
        return JMart(browser=self.browser, url=self.browser.current_url)

    def go_to_tv_audio_video_and_photo_jmart_page(self):
        # self.browser.execute_script(f"window.scrollBy(0, 1400);")
        # time.sleep(3)
        button_tv_audio_video_and_photo = self.browser.find_element(*StoreSectionLocators.TV_AUDIO_VIDEO_AND_PHOTO)
        button_tv_audio_video_and_photo.click()
        return JMart(browser=self.browser, url=self.browser.current_url)
