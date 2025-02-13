from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from confest import driver
from locators import PersonalPageLoginLocators, BurgerPartsNames, LogOut
import time

class TestGoToPersonalAccount:
    def test_user_click_to_personal_account_success(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*PersonalPageLoginLocators.PERSONAL_PAGE_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(PersonalPageLoginLocators.EMAIL_INPUT))

        driver.find_element(*PersonalPageLoginLocators.EMAIL_INPUT).send_keys('aleksandra_drobotun_18@yandex.ru')
        driver.find_element(*PersonalPageLoginLocators.PASSWORD_INPUT).send_keys('drobotun123')
        driver.find_element(*PersonalPageLoginLocators.LOG_IN_BUTTON).click()
        driver.find_element(*PersonalPageLoginLocators.PERSONAL_PAGE_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(LogOut.LOG_OUT_BUTTON))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'
