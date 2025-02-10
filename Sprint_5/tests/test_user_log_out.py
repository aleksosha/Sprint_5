import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import locators
from tests.locators import LogOut
from confest import driver


def test_user_log_out(driver):
    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.find_element(*LogOut.LOG_INTO_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 5).until(expected_conditions.url_contains('/login'))
    driver.find_element(*LogOut.EMAIL_INPUT).send_keys('aleksandra_drobotun_18@yandex.ru')
    driver.find_element(*LogOut.PASSWORD_INPUT).send_keys('drobotun123')
    driver.find_element(*LogOut.LOG_IN_BUTTON).click()
    WebDriverWait(driver, 5).until(expected_conditions.url_contains('.site'))
    driver.find_element(*LogOut.PERSONAL_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/div/nav/ul/li[3]/button')))
    driver.find_element(*LogOut.LOG_OUT_BUTTON).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/div/h2')))