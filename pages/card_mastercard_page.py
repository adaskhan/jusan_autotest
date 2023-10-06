import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage
from src_pages import MasterCardLocators


class CardMastercardPage(BasePage):

    def go_to_order_mastercard(self):
        self.browser.execute_script(f"window.scrollBy(0, 1000);")
        time.sleep(3)
        order_btn = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(MasterCardLocators.ORDER_BTN)
        )
        order_btn.click()
        self.get_map_of_all_locations_jusan()

    def get_map_of_all_locations_jusan(self):
        assert WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(MasterCardLocators.MAP)
        ), "Map is not opened"

    def check_info_after_opening_mastercard_page(self):
        assert "Особые возможности и привилегии по всему миру" == WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(MasterCardLocators.RANDOM_TEXT_FOR_CHECKING_1)
        ).text and "MasterCard World Elite" == WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(MasterCardLocators.RANDOM_TEXT_FOR_CHECKING_2)
        ).text
