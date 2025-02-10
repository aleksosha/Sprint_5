
from selenium.webdriver.common.by import By


class RegistrationPageLocators:
    NAME_INPUT = (By.XPATH, '//label[text()="Имя"]/following-sibling::input')  # Поле для ввода имени
    EMAIL_INPUT = (By.XPATH, '//label[text()="Email"]/following-sibling::input')  # Поле для ввода email
    PASSWORD_INPUT = (By.XPATH, '//label[text()="Пароль"]/following-sibling::input')  # Поле для ввода пароля
    REGISTER_BUTTON = (By.XPATH, '//button[text()="Зарегистрироваться"]')  # Кнопка "Зарегистрироваться"

class LoginPageLocators:
    LOG_IN_ACCOUNT_BUTTON = (By.XPATH, '//button[text()="Войти в аккаунт"]') # Кнопка "Войти в аккаунт"
    EMAIL_INPUT = (By.XPATH, '//label[text()="Email"]/following-sibling::input')  # Поле для ввода email
    PASSWORD_INPUT = (By.XPATH, '//label[text()="Пароль"]/following-sibling::input')  # Поле для ввода пароля
    LOG_IN_BUTTON = (By.XPATH, '//button[contains(text(), "Войти")]') # Кнопка "Войти"

class PersonalPageLoginLocators:
    PERSONAL_PAGE_BUTTON = (By.XPATH, '//*[@id="root"]/div/header/nav/a/p') # Кнопка "Личный кабинет"
    EMAIL_INPUT = (By.XPATH, '//label[text()="Email"]/following-sibling::input')  # Поле для ввода email
    PASSWORD_INPUT = (By.XPATH, '//label[text()="Пароль"]/following-sibling::input') # Поле для ввода пароля
    LOG_IN_BUTTON = (By.XPATH, '//button[contains(text(), "Войти")]') # Кнопка войти
    PERSONAL_PAGE = (By.XPATH, '//*[@id="root"]/div/main/div/nav/ul/li[1]/a') # Кнопка "Личныйй кабиент"

class LogInThroughRegisterPage:
    LOG_IN_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/div/div/p/a') # Кнопка "Войти"
    EMAIL_INPUT = (By.XPATH, '//label[text()="Email"]/following-sibling::input')  # Поле для ввода email
    PASSWORD_INPUT = (By.XPATH, '//label[text()="Пароль"]/following-sibling::input') # Поле для ввода пароля
    LOG_IN_REGISTRATION_BUTTON = (By.XPATH, '//button[contains(text(), "Войти")]') # Кнопка войти через страницу регистрации

class RestorePassword:
    FORGOT_PASSWORD_BUTTON = (By.XPATH, './/a[text()="Восстановить пароль"]') # Кнопка восстановить пароль
    EMAIL_INPUT = (By.XPATH, '//label[text()="Email"]/following-sibling::input')  # Поле для ввода email
    RESTORE_PASSWORD_BUTTON = (By.XPATH, '//button[text()="Восстановить"]') # Кнопка восстановить

class LogOut:
    LOG_INTO_ACCOUNT_BUTTON = (By.XPATH, '//button[text()="Войти в аккаунт"]') # Кнопка войти
    EMAIL_INPUT = (By.XPATH, '//label[text()="Email"]/following-sibling::input')  # Поле для ввода email
    PASSWORD_INPUT = (By.XPATH, '//label[text()="Пароль"]/following-sibling::input') # Поле для ввода пароля
    LOG_IN_BUTTON = (By.XPATH, '//button[contains(text(), "Войти")]') # Кнопка войти
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, '//*[@id ="root"]/div/header/nav/a/p') # Кнопка "Личный кабинет"
    LOG_OUT_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/div/nav/ul/li[3]/button') # Кнопка "Выход"

class BurgerPartsNames:
    SAUCES = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[2]/span') # Кнопка "Соусы"
    BUNS = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[1]/span') # Кнопка "Булки"
    TOPPINGS = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[3]/span') # Кнопка "Начинки"

