import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from confest import driver
from locators import BurgerPartsNames


class TestConstructor:

    def test_go_to_buns_constructor(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(BurgerPartsNames.BUNS)).click()
        assert WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(BurgerPartsNames.BUNS)).text == 'Булки'

    def test_go_to_sauces_constructor(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(BurgerPartsNames.SAUCES)).click()
        assert WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(BurgerPartsNames.SAUCES)).text == 'Соусы'


    def test_go_to_toppings_constructor(self, driver):

        driver.get('https://stellarburgers.nomoreparties.site/')

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(BurgerPartsNames.TOPPINGS)).click()
        assert WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(BurgerPartsNames.LABEL_TOPPINGS)).text == 'Начинки'
