from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from tests.confest import driver
from tests.locators import LoginPageLocators, PersonalPageLoginLocators, LogInThroughRegisterPage, RestorePassword


def test_login_through_main_page(driver):
    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.find_element(*LoginPageLocators.LOG_IN_ACCOUNT_BUTTON).click()

    WebDriverWait(driver, 5).until(expected_conditions.url_contains('/login'))

    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys('aleksandra_drobotun_18@yandex.ru')
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys('drobotun123')

    driver.find_element(*LoginPageLocators.LOG_IN_BUTTON).click()

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/section[1]/h1')))

    driver.quit()

def test_login_through_personal_account(driver):
    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.find_element(*PersonalPageLoginLocators.PERSONAL_PAGE_BUTTON).click()

    WebDriverWait(driver, 5).until(expected_conditions.url_contains('/login'))

    driver.find_element(*PersonalPageLoginLocators.EMAIL_INPUT).send_keys('aleksandra_drobotun_18@yandex.ru')
    driver.find_element(*PersonalPageLoginLocators.PASSWORD_INPUT).send_keys('drobotun123')

    driver.find_element(*PersonalPageLoginLocators.LOG_IN_BUTTON).click()

    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/section[1]/h1')))

def test_login_through_registration_page(driver):
    driver.get('https://stellarburgers.nomoreparties.site/register')
    driver.find_element(*LogInThroughRegisterPage.LOG_IN_BUTTON).click()

    driver.find_element(*LogInThroughRegisterPage.EMAIL_INPUT).send_keys('aleksandra_drobotun_18@yandex.ru')
    driver.find_element(*LogInThroughRegisterPage.PASSWORD_INPUT).send_keys('drobotun123')

    driver.find_element(*LogInThroughRegisterPage.LOG_IN_REGISTRATION_BUTTON).click()

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/section[1]/h1')))

def test_login_through_password_recovery_form(driver):
    driver.get('https://stellarburgers.nomoreparties.site/login')
    driver.find_element(*RestorePassword.FORGOT_PASSWORD_BUTTON).click()
    WebDriverWait(driver, 15).until(expected_conditions.url_contains('/forgot-password'))
    driver.find_element(*RestorePassword.EMAIL_INPUT).send_keys('aleksandra_drobotun_18@yandex.ru')
    driver.find_element(*RestorePassword.RESTORE_PASSWORD_BUTTON)
