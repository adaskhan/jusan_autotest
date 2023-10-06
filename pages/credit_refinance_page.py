from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage
from src_pages import CreditRefinanceLocators


class CreditRefinancePage(BasePage):

    def go_to_order_credit_refinance(self):
        order_btn = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(CreditRefinanceLocators.ORDER_BTN)
        )
        order_btn.click()
        self.get_qr_code()

    def get_qr_code(self):
        assert WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(CreditRefinanceLocators.QRCODE)
        )

    def check_close_qr_code(self):
        assert WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(CreditRefinanceLocators.CLOSE_QRCODE)
        ), "QR Code does not closed"

    def close_qr_code(self):
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(CreditRefinanceLocators.CLOSE_QRCODE)
        ).click()

    def check_info_after_closing_qr_code(self):
        assert "Выгодные условия для комфортного погашения" == WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(CreditRefinanceLocators.RANDOM_TEXT_FOR_CHECKING_1)
        ).text and "Рефинансирование займов" == WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(CreditRefinanceLocators.RANDOM_TEXT_FOR_CHECKING_2)
        ).text
