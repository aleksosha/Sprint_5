from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from confest import driver
from locators import LoginPageLocators, PersonalPageLoginLocators, RestorePassword, LogInThroughRegisterPageLocators


class TestLogIn:
    def test_login_through_main_page(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*LoginPageLocators.LOG_IN_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT))
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys('aleksandra_drobotun_18@yandex.ru')
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys('drobotun123')
        driver.find_element(*LoginPageLocators.LOG_IN_BUTTON).click()

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    def test_login_through_personal_account(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*PersonalPageLoginLocators.PERSONAL_PAGE_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(PersonalPageLoginLocators.EMAIL_INPUT))

        driver.find_element(*PersonalPageLoginLocators.EMAIL_INPUT).send_keys('aleksandra_drobotun_18@yandex.ru')
        driver.find_element(*PersonalPageLoginLocators.PASSWORD_INPUT).send_keys('drobotun123')

        driver.find_element(*PersonalPageLoginLocators.LOG_IN_BUTTON).click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'


    def test_login_through_registration_page(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/register')

        driver.find_element(*LogInThroughRegisterPageLocators.LOG_IN_BUTTON).click()
        driver.find_element(*LogInThroughRegisterPageLocators.EMAIL_INPUT).send_keys('aleksandra_drobotun_18@yandex.ru')
        driver.find_element(*LogInThroughRegisterPageLocators.PASSWORD_INPUT).send_keys('drobotun123')

        driver.find_element(*LogInThroughRegisterPageLocators.LOG_IN_REGISTRATION_BUTTON).click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'


    def test_login_through_password_recovery_form(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/login')
        driver.find_element(*RestorePassword.FORGOT_PASSWORD_BUTTON).click()
        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(RestorePassword.RESTORE_PASSWORD_BUTTON))
        driver.find_element(*RestorePassword.EMAIL_INPUT).send_keys('aleksandra_drobotun_18@yandex.ru')
        driver.find_element(*RestorePassword.RESTORE_PASSWORD_BUTTON).click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/forgot-password'
