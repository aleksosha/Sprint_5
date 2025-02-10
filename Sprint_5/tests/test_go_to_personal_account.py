from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from tests.confest import driver
from tests.locators import PersonalPageLoginLocators
import time

def test_user_click_to_personal_account_success(driver):
    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.find_element(*PersonalPageLoginLocators.PERSONAL_PAGE_BUTTON).click()

    WebDriverWait(driver, 5).until(expected_conditions.url_contains('/login'))

    driver.find_element(*PersonalPageLoginLocators.EMAIL_INPUT).send_keys('aleksandra_drobotun_18@yandex.ru')
    driver.find_element(*PersonalPageLoginLocators.PASSWORD_INPUT).send_keys('drobotun123')
    driver.find_element(*PersonalPageLoginLocators.LOG_IN_BUTTON).click()
    WebDriverWait(driver, 5).until(expected_conditions.url_contains('.site'))
    driver.find_element(*PersonalPageLoginLocators.PERSONAL_PAGE_BUTTON).click()
    time.sleep(2)
