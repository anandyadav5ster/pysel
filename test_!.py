import pytest
from selenium import webdriver
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

global driver
options = Options()
options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"
path = "../Drivers/chromedriver.exe"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('https://lambdatest.github.io/sample-todo-app/')
driver.maximize_window()
driver.quit()