#!/usr/bin/env python3
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def start():
    service = Service(executable_path="/chromedriver-linux64/chromedriver")
    options = webdriver.ChromeOptions()
    for _ in [
        'headless',
        'window-size=1920x1080',
        'disable-gpu',
        'no-sandbox',
        'disable-dev-shm-usage',
    ]:
        options.add_argument(_)
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)
    driver.set_page_load_timeout(10)
    return driver

def login(pw):
    time.sleep(5)
    driver.get('http://127.0.0.1:5000/login')
    driver.implicitly_wait(10)
    driver.find_element('id', 'username').send_keys('admin')
    driver.find_element('id', 'password').send_keys(pw)
    driver.find_element('xpath', '/html/body/div/div/form[1]/button').click()

def read_reports():
    driver.get('http://127.0.0.1:5000/reports')
    driver.implicitly_wait(10)
    driver.set_page_load_timeout(10)

driver = start()
