import time
url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button_add_to_basket_should_exist(browser):
    browser.get(url)
    time.sleep(30)
    buttons = len(browser.find_elements_by_css_selector(".btn-add-to-basket"))
    assert buttons > 0, 'The button "Add to basket" is not found'