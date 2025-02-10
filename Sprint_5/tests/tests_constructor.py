import pytest
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from confest import driver
from tests.locators import BurgerPartsNames



def test_go_to_buns_constructor(driver):
    driver.get('https://stellarburgers.nomoreparties.site/')

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/h2[1]')))

    driver.find_element(*BurgerPartsNames.SAUCES).click()
    time.sleep(2)
    driver.find_element(*BurgerPartsNames.BUNS).click()
    time.sleep(2)
    driver.find_element(BurgerPartsNames.TOPPINGS).click()
    time.sleep(2)
    driver.find_element(BurgerPartsNames.BUNS).click()
    time.sleep(2)


def test_go_to_sauces_constructor(driver):
    driver.get('https://stellarburgers.nomoreparties.site/')

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/h2[1]')))

    driver.find_element(*BurgerPartsNames.SAUCES).click()
    time.sleep(5)
    driver.find_element(*BurgerPartsNames.TOPPINGS).click()
    time.sleep(5)
    driver.find_element(*BurgerPartsNames.SAUCES).click()
    time.sleep(5)
    driver.find_element(*BurgerPartsNames.BUNS).click()
    time.sleep(5)


def test_go_to_toppings_constructor(driver):
    driver.get('https://stellarburgers.nomoreparties.site/')

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/h2[1]')))

    driver.find_element(*BurgerPartsNames.SAUCES).click()
    time.sleep(5)
    driver.find_element(*BurgerPartsNames.TOPPINGS).click()
    time.sleep(5)
    driver.find_element(BurgerPartsNames.BUNS).click()
    time.sleep(5)
    driver.find_element(*BurgerPartsNames.TOPPINGS).click()
    time.sleep(5)
