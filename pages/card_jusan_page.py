from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage
from src_pages import CardJusanLocators


class CardJusanPage(BasePage):

    def go_to_open_card(self):
        order_btn = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(CardJusanLocators.ORDER_BTN)
        )
        order_btn.click()
        self.get_qr_code()

    def get_qr_code(self):
        assert WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(CardJusanLocators.QRCODE)
        )

    def check_close_qr_code(self):
        assert WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(CardJusanLocators.CLOSE_QRCODE)
        ), "QR Code does not closed"

    def close_qr_code(self):
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(CardJusanLocators.CLOSE_QRCODE)
        ).click()

    def check_info_after_closing_qr_code(self):
        assert "Чем больше транзакций, тем больше бонусов" == WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(CardJusanLocators.RANDOM_TEXT_FOR_CHECKING_1)
        ).text and "Карта Jusan" == WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(CardJusanLocators.RANDOM_TEXT_FOR_CHECKING_2)
        ).text

