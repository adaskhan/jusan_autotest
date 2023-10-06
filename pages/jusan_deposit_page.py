from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage
from src_pages import DepositPageLocators


class JusanDepositPage(BasePage):

    def go_to_order_deposit(self):
        order_btn = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(DepositPageLocators.ORDER_BTN)
        )
        order_btn.click()
        self.get_qr_code()

    def get_qr_code(self):
        assert WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(DepositPageLocators.QRCODE)
        )

    def check_close_qr_code(self):
        assert WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(DepositPageLocators.CLOSE_QRCODE)
        ), "QR Code does not closed"

    def close_qr_code(self):
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(DepositPageLocators.CLOSE_QRCODE)
        ).click()

    def check_info_after_closing_qr_code(self):
        assert "Управляйте своими сбережениями онлайн" == WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(DepositPageLocators.RANDOM_TEXT_FOR_CHECKING_1)
        ).text
