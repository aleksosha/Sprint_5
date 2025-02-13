from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from Sprint_5.Sprint_5.tests.locators import LoginPageLocators
from locators import LogOut
from confest import driver


class TestLogOut:
    def test_user_log_out(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*LogOut.LOG_INTO_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.url_contains('/login'))
        driver.find_element(*LogOut.EMAIL_INPUT).send_keys('aleksandra_drobotun_18@yandex.ru')
        driver.find_element(*LogOut.PASSWORD_INPUT).send_keys('drobotun123')
        driver.find_element(*LogOut.LOG_IN_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.url_contains('.site'))
        driver.find_element(*LogOut.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(LogOut.LOG_OUT_BUTTON))
        driver.find_element(*LogOut.LOG_OUT_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(LoginPageLocators.LOG_IN_BUTTON))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
