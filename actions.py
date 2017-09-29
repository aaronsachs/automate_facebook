from selenium import webdriver
from home_page import HomePage
from navbar import NavBar

# Login to account with appropriate credentials
def login(email, password, driver, teardown = False):
    hp = HomePage(driver)
    hp.email_input(email)
    hp.password_input(password)
    hp.login_button()
    if teardown: hp.teardown()
    return driver

# Logout of account
def logout(driver):
    nb = NavBar(driver)
    nb.logout_button()
    

