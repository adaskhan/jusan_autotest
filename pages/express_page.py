import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage
from src_pages import ExpressPageLocators


class ExpressPage(BasePage):

    def go_to_order_credit(self):
        order_btn = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(ExpressPageLocators.ORDER_BTN)
        )
        order_btn.click()
        self.get_qr_code()

    def get_qr_code(self):
        assert WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(ExpressPageLocators.QRCODE)
        )

    def check_close_qr_code(self):
        assert WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(ExpressPageLocators.CLOSE_QRCODE)
        ), "QR Code does not closed"

    def close_qr_code(self):
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(ExpressPageLocators.CLOSE_QRCODE)
        ).click()

    def check_info_after_closing_qr_code(self):
        assert "Онлайн без залога и на любые цели" == WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(ExpressPageLocators.RANDOM_TEXT_FOR_CHECKING_1)
        ).text and "Онлайн кредит" == WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(ExpressPageLocators.RANDOM_TEXT_FOR_CHECKING_2)
        ).text

    def check_monthly_payment(self):
        self.browser.execute_script(f"window.scrollBy(0, 1000);")
        time.sleep(3)
        self.enter_sum_credit(1300000)
        time.sleep(5)
        monthly_payment = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(ExpressPageLocators.MONTHLY_PAYMENT)
        ).text
        assert "450 781.00" == monthly_payment, f"Monthly payment is bug, {monthly_payment}"

    def enter_sum_credit(self, summa):
        sum_of_credit = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(ExpressPageLocators.SUM_CREDIT)
        ).clear()
        sum_of_credit.send_keys(summa)

    def get_credit(self):
        self.browser.execute_script(f"window.scrollBy(0, 1000);")
        time.sleep(3)
        order_credit_btn = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(ExpressPageLocators.GET_CREDIT_BTN)
        )
        order_credit_btn.click()
        self.get_qr_code()

    def check_info_after_closing_qr_code_calculator_section(self):
        assert "Калькулятор кредита" == WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(ExpressPageLocators.TITLE_CALCULATOR)
        ).text

    def check_get_credit_gold_btn(self):
        self.browser.execute_script(f"window.scrollBy(0, 600);")
        time.sleep(3)
        order_credit_btn = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(ExpressPageLocators.ORDER_GOLD_BTN)
        )
        order_credit_btn.click()
        self.get_qr_code()

    def send_request_to_manager(self):
        self.browser.execute_script(f"window.scrollBy(0, 3200);")
        time.sleep(3)
        region_input = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(ExpressPageLocators.REGION_FORM)
        )
        region_input.send_keys("Алматы")
        iin_input = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(ExpressPageLocators.IIN_FORM)
        )
        iin_input.send_keys("030211501424")
        name_input = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(ExpressPageLocators.NAME_FORM)
        )
        name_input.send_keys("TEST")
        phone_input = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(ExpressPageLocators.PHONE_FORM)
        )
        phone_input.send_keys("7777777777")

        submit_request_btn = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(ExpressPageLocators.SUBMIT_REQUEST_BTN)
        )
        submit_request_btn.click()

        thank_msg = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(ExpressPageLocators.THANK_MESSAGE)
        ).text

        close_thank_msg = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(ExpressPageLocators.CLOSE_THANK_MESSAGE)
        )
        close_thank_msg.click()

        assert "Спасибо" in thank_msg, "Request haven't been sent"
