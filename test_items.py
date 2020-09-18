import time
from selenium.common.exceptions import NoSuchElementException


link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_add_to_basket_exists_for_different_languages(browser):
    browser.implicitly_wait(10)
    browser.get(link)
    time.sleep(30)
    result=True
    try:
        browser.find_element_by_css_selector('.btn-add-to-basket')
    except NoSuchElementException:
        result=False
    assert result == True, "'Add-to-basket' button is not found"
    

