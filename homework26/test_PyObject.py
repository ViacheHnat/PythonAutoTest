import time
from homework26.conftest import driver
from homework26.test_homework26 import PageObject


def test_google_search_with_cookies(driver, open_start_page):
    registration_page = PageObject(driver)
    registration_page.click_button()
    registration_page.enterName()
    registration_page.enterLastName()
    registration_page.enterEmail()
    registration_page.enterPassword()
    registration_page.enterPasswordAgain()
    registration_page.clickRegistration()
    time.sleep(3)
    assert 'https://guest:welcome2qauto@qauto2.forstudy.space/panel/garage' == registration_page.current_url()
    time.sleep(3)

