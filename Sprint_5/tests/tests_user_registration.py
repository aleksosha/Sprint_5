from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
from tests.locators import RegistrationPageLocators
from confest import driver


def test_successful_registration(driver):
    driver.get('https://stellarburgers.nomoreparties.site/register')

    driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys('Александра')

    driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys('aleksandra_drobotun_18_9@yandex.ru')

    driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys('drobot')

    driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/section[1]/h1')))



def test_registration_name_is_empty(driver):
    driver.get('https://stellarburgers.nomoreparties.site/register')

    driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys('aleksandra_drobotun_18_10@yandex.ru')

    driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys('drobotun123')

    driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/section[1]/h1')))



def test_registration_invalid_email_no_separator(driver):
    driver.get('https://stellarburgers.nomoreparties.site/register')

    driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys('Александра')

    driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys('aleksandra_drobotun_18_11yandex.ru')

    driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys('drobotun123')

    driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/section[1]/h1')))




def test_registration_invalid_email_no_domain_name(driver):
    driver.get('https://stellarburgers.nomoreparties.site/register')

    driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys('Александра')

    driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys('aleksandra_drobotun_18_12@yandexru')

    driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys('drobotun123')

    driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/section[1]/h1')))



def test_registration_password_contains_seven_symbols(driver):
    driver.get('https://stellarburgers.nomoreparties.site/register')

    driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys('Александра')

    driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys('aleksandra_drobotun_18_13@yandex.ru')

    driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys('drobotu')

    driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/section[1]/h1')))



def test_registration_password_contains_five_symbols(driver):
    driver.get('https://stellarburgers.nomoreparties.site/register')

    driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys('Александра')

    driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys('aleksandra_drobotun_18_14@yandex.ru')

    driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys('drobo')

    driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

    time.sleep(4)
    WebDriverWait(driver, 5).until(
        lambda error: 'Некорректный пароль' in error.page_source
    )



def test_registration_password_contains_one_symbols(driver):
    driver.get('https://stellarburgers.nomoreparties.site/register')

    river.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys('Александра')

    driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys('aleksandra_drobotun_18_15@yandex.ru')

    driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys('d')

    driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()
    time.sleep(4)
    WebDriverWait(driver, 5).until(
        lambda error: 'Некорректный пароль' in error.page_source
    )



def test_registration_password_is_empty(driver):
    driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys('Александра')

    driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys('aleksandra_drobotun_16@yandex.ru')

    driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys('drobo')

    driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/section[1]/h1')))

