
from selenium.webdriver.common.by import By


class RegistrationPageLocators:
    NAME_INPUT = (By.XPATH, '//div[contains(@class, "input")][.//label[text()="Имя"]]//input')  # Поле для ввода имени
    EMAIL_INPUT = (By.XPATH, '//div[label[contains(text(),"Email")]]/input')  # Поле для ввода email
    PASSWORD_INPUT = (By.XPATH, '//div[label[contains(text(),"Пароль")]]/input')  # Поле для ввода пароля
    REGISTER_BUTTON = (By.XPATH, '//button[text()="Зарегистрироваться"]')  # Кнопка "Зарегистрироваться"

class LoginPageLocators:
    LOG_IN_ACCOUNT_BUTTON = (By.XPATH, '//button[text()="Войти в аккаунт"]') # Кнопка "Войти в аккаунт"
    EMAIL_INPUT = (By.XPATH, '//div[label[contains(text(),"Email")]]/input')  # Поле для ввода email
    PASSWORD_INPUT = (By.XPATH, '//div[label[contains(text(),"Пароль")]]/input')  # Поле для ввода пароля
    LOG_IN_BUTTON = (By.XPATH, '//button[contains(text(), "Войти")]') # Кнопка "Войти"

class PersonalPageLoginLocators:
    PERSONAL_PAGE_BUTTON = (By.XPATH, '//a[contains(@class, "AppHeader_header__link") and @href="/account"]/p') # Кнопка "Личный кабинет"
    EMAIL_INPUT = (By.XPATH, '//div[label[contains(text(),"Email")]]/input')  # Поле для ввода email
    PASSWORD_INPUT = (By.XPATH, '//div[label[contains(text(),"Пароль")]]/input')  # Поле для ввода пароля
    LOG_IN_BUTTON = (By.XPATH, '//button[contains(text(), "Войти")]') # Кнопка войти
    PERSONAL_PAGE = (By.XPATH, '//a[contains(@class, "AppHeader_header__link") and @href="/account"]/p') # Кнопка "Личныйй кабинет"

class LogInThroughRegisterPageLocators:
    LOG_IN_BUTTON = (By.XPATH, '//a[contains(@class, "Auth_link") and text()="Войти"]') # Кнопка "Войти"
    EMAIL_INPUT = (By.XPATH, '//div[label[contains(text(),"Email")]]/input')  # Поле для ввода email
    PASSWORD_INPUT = (By.XPATH, '//div[label[contains(text(),"Пароль")]]/input')  # Поле для ввода пароля
    LOG_IN_REGISTRATION_BUTTON = (By.XPATH, '//button[contains(text(), "Войти")]') # Кнопка войти через страницу регистрации

class RestorePassword:
    FORGOT_PASSWORD_BUTTON = (By.XPATH, './/a[text()="Восстановить пароль"]') # Кнопка восстановить пароль
    EMAIL_INPUT = (By.XPATH, '//div[label[contains(text(),"Email")]]/input')  # Поле для ввода email
    RESTORE_PASSWORD_BUTTON = (By.XPATH, '//button[text()="Восстановить"]') # Кнопка восстановить

class LogOut:
    LOG_INTO_ACCOUNT_BUTTON = (By.XPATH, '//button[text()="Войти в аккаунт"]') # Кнопка войти
    EMAIL_INPUT = (By.XPATH, '//div[label[contains(text(),"Email")]]/input')  # Поле для ввода email
    PASSWORD_INPUT = (By.XPATH, '//div[label[contains(text(),"Пароль")]]/input') # Поле для ввода пароля
    LOG_IN_BUTTON = (By.XPATH, '//button[contains(text(), "Войти")]') # Кнопка войти
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, '//a[contains(@class, "AppHeader_header__link") and @href="/account"]/p') # Кнопка "Личный кабинет"
    LOG_OUT_BUTTON = (By.XPATH, '//button[contains(text(), "Выход")]') # Кнопка "Выход"

class BurgerPartsNames:

    SAUCES = (By.XPATH, '//span[text()="Соусы"]')  # Кнопка "Соусы"
    BUNS = (By.XPATH, '//span[text()="Булки"]')  # Кнопка "Булки"
    TOPPINGS = (By.XPATH, '//span[text()="Начинки"]')  # Кнопка "Начинки"

    LABEL_TOPPINGS = (By.XPATH, '//h2[text()="Начинки"]')  # подзаголовок "Начинки" в таблице
    LABEL_SAUCES = (By.XPATH, '//h2[text()="Соусы"]')  # подзаголовок "Соусы" в таблице
    LABEL_BUNS = (By.XPATH, '//h2[text()="Булки"]')  # подзаголовок "Булки" в таблице