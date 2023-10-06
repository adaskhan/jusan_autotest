from pages.main_page import Products, Store


def test_client_can_order_express_credit(browser):
    link = "http://jusan.kz"
    page = Products(browser, link)
    page.open()

    express_credit = page.go_to_online_credit_page()
    express_credit.go_to_order_credit()
    express_credit.check_close_qr_code()
    express_credit.close_qr_code()
    express_credit.check_info_after_closing_qr_code()

    # order_credit.check_monthly_payment()
    express_credit.get_credit()
    express_credit.check_close_qr_code()
    express_credit.close_qr_code()
    express_credit.check_info_after_closing_qr_code_calculator_section()

    express_credit.check_get_credit_gold_btn()
    express_credit.close_qr_code()


# def test_client_can_send_request_to_manager(browser):
#     link = "http://jusan.kz"
#     page = MainPage(browser, link)
#     page.open()
#
#     express_credit = page.go_to_online_credit_page()
#     express_credit.send_request_to_manager()


def test_client_can_order_deposit(browser):
    link = "http://jusan.kz"
    page = Products(browser, link)
    page.open()
    order_deposit = page.go_to_jusan_deposit_page()
    order_deposit.go_to_order_deposit()
    order_deposit.check_close_qr_code()
    order_deposit.close_qr_code()
    order_deposit.check_info_after_closing_qr_code()


def test_client_can_open_card(browser):
    link = "http://jusan.kz"
    page = Products(browser, link)
    page.open()
    open_card = page.go_to_card_jusan_page()
    open_card.go_to_open_card()
    open_card.check_close_qr_code()
    open_card.close_qr_code()
    open_card.check_info_after_closing_qr_code()


def test_client_can_order_credit_reference(browser):
    link = "http://jusan.kz"
    page = Products(browser, link)
    page.open()
    order_credit_refinance = page.go_to_credit_refinance_page()
    order_credit_refinance.go_to_order_credit_refinance()
    order_credit_refinance.check_close_qr_code()
    order_credit_refinance.close_qr_code()
    order_credit_refinance.check_info_after_closing_qr_code()


def test_client_can_order_mastercard(browser):
    link = "http://jusan.kz"
    page = Products(browser, link)
    page.open()
    order_mastercard = page.go_to_card_mastercard_page()
    order_mastercard.check_info_after_opening_mastercard_page()
    order_mastercard.go_to_order_mastercard()
    order_mastercard.get_map_of_all_locations_jusan()


def test_client_can_go_to_jmart_page(browser):
    link = "http://jusan.kz"
    page = Store(browser, link)
    page.open()

    jmart_laptops_and_computers = page.go_to_laptops_and_computers_jmart_page()
    jmart_laptops_and_computers.check_current_url()

    jmart_home_furniture = page.go_to_home_furniture_jmart_page()
    jmart_home_furniture.check_current_url()

    jmart_smartphones_and_gadget = page.go_to_smartphones_and_gadget_jmart_page()
    jmart_smartphones_and_gadget.check_current_url()

    jmart_sport_and_tourism = page.go_to_sport_and_tourism_jmart_page()
    jmart_sport_and_tourism.check_current_url()

    jmart_home_appliances = page.go_to_home_appliances_jmart_page()
    jmart_home_appliances.check_current_url()

    jmart_tv_audio_video_and_photo = page.go_to_tv_audio_video_and_photo_jmart_page()
    jmart_tv_audio_video_and_photo.check_current_url()


from PIL import Image
from selenium import webdriver

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.allure.step("Capture screenshot")
def capture_screenshot(browser, screenshot_path):
    browser.save_screenshot(screenshot_path)

@allure.attachment_type("image/png")
def attach_screenshot(screenshot_path):
    with open(screenshot_path, "rb") as file:
        return file.read()

def test_pixel_accuracy(browser):
    # Open the web page
    browser.get('https://example.com')

    # Capture a screenshot of the web page
    screenshot_path = 'screenshot.png'
    capture_screenshot(browser, screenshot_path)

    # Open the reference image
    reference_image_path = 'reference_image.png'
    reference_image = Image.open(reference_image_path)

    # Open the captured screenshot
    screenshot_image = Image.open(screenshot_path)

    # Compare the images pixel by pixel
    diff = ImageChops.difference(reference_image, screenshot_image)

    # Calculate the percentage difference
    percentage_diff = (100.0 * count_diff_pixels(diff)) / reference_image.size[0] * reference_image.size[1]

    # Define a threshold for acceptable differences
    threshold = 1.0

    # Attach the screenshot to the Allure report
    allure.attach(attach_screenshot(screenshot_path), name="Screenshot", attachment_type=allure.attachment_type.PNG)

    # Assert if the percentage difference exceeds the threshold
    assert percentage_diff <= threshold, f"Pixel accuracy test failed. Percentage difference: {percentage_diff}%"

def count_diff_pixels(image):
    """
    Counts the number of differing pixels in the given image.
    """
    diff_pixels = 0
    diff_data = image.getdata()
    for item in diff_data:
        if item != (0, 0, 0, 0):
            diff_pixels += 1
    return diff_pixels
