from .base_page import BasePage


class JMart(BasePage):

    def check_current_url(self):
        current_jmart_url = self.url
        self.browser.back()
        assert 'jmart' in current_jmart_url
