from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import RegistrationPageLocators, LoginPageLocators
from confest import driver
from helpers import generate_unique_email

class TestUserRegistration:
    def test_successful_registration(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/register')

        driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys('Александра')
        unique_email = generate_unique_email()
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(unique_email)
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys('drobot')
        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(LoginPageLocators.LOG_IN_BUTTON))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    def test_registration_name_is_empty(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/register')

        unique_email = generate_unique_email()
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(unique_email)
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys('drobotun123')
        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/register'

    def test_registration_invalid_email_no_separator(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/register')

        driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys('Александра')
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys('aleksandra_drobotun_18_11yandex.ru')
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys('drobotun123')
        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/register'


    def test_registration_invalid_email_no_domain_name(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/register')

        driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys('Александра')
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys('aleksandra_drobotun_18_12@yandexru')
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys('drobotun123')
        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/register'



    def test_registration_password_contains_seven_symbols(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/register')

        driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys('Александра')
        unique_email = generate_unique_email()
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(unique_email)
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys('drobotu')
        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(LoginPageLocators.LOG_IN_BUTTON))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'


    def test_registration_password_contains_five_symbols(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/register')

        driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys('Александра')
        unique_email = generate_unique_email()
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(unique_email)
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys('drobo')
        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

        WebDriverWait(driver, 5).until(lambda error: 'Некорректный пароль' in error.page_source)

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/register'

    def test_registration_password_contains_one_symbols(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/register')

        driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys('Александра')
        unique_email = generate_unique_email()
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(unique_email)
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys('d')
        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

        WebDriverWait(driver, 5).until(lambda error: 'Некорректный пароль' in error.page_source)

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/register'

    def test_registration_password_is_empty(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/register')
        driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys('Александра')

        unique_email = generate_unique_email()
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(unique_email)
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys('drobo')
        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/register'

