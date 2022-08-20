from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
import time

chrome_driver_path = r"C:\Users\Gumo\Desktop\Git\Develop\chromedriver"
driver = webdriver.Chrome(service=ChromeService(chrome_driver_path))
driver.get("https://mtsac.instructure.com/")

username=driver.find_element(by=By.ID, value="usernameUserInput")
username.send_keys("xchen37")

passw=driver.find_element(by=By.ID, value="password")
passw.send_keys("")

signin=