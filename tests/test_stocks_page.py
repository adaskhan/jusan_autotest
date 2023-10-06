from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages import base_page


def test_pagination(browser):
    link = "http://jusan.kz/stocks"
    page = base_page.BasePage(browser, link)
    page.open()

    pagination_element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//ul[@class='pagination']"))
        )
    total_pages = int(pagination_element.text.split()[-1])

    cards = []
    for page in range(1, total_pages + 1):
        if page != 1:
            browser.get(f"http://jusan.kz/stocks?page={page}")

        card_elements = WebDriverWait(browser, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@class='card-custom-body card-body']"))
        )

        for card_element in card_elements:
            card_data = {
                "title": card_element.find_element(By.CLASS_NAME, "card-title").text,
                "links": card_element.find_element(
                    By.XPATH, "//div[@class='card-custom-body card-body']/a"
                ).get_attribute('href')
            }
            cards.append(card_data)

    assert len(cards) == 9, f"Длина не правильно, {len(cards)}"
    print(cards)
