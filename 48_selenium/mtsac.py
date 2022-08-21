from turtle import title
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
import time

# path for token
path_pixela = r"C:\Users\Gumo\Desktop\Git\Notebook\keys\mtsac.txt"
# load token
with open(path_pixela,"r") as newsfile:
    TOKEN = newsfile.readline()


chrome_driver_path = r"C:\Users\Gumo\Desktop\Git\Develop\chromedriver"
driver = webdriver.Chrome(service=ChromeService(chrome_driver_path))
driver.get("https://mtsac.instructure.com/")

username=driver.find_element(by=By.ID, value="usernameUserInput")
username.send_keys("xchen37")

passw=driver.find_element(by=By.ID, value="password")
passw.send_keys(TOKEN)

signin=driver.find_element(by=By.XPATH, value="/html/body/main/div/div[2]/div/form/div[6]/div[5]/div[2]/button")
signin.click()

course=driver.find_element(by=By.XPATH, value="/html/body/div[3]/div[2]/div/div[2]/div[1]/div/div/div[5]/div/div/div[1]/div/a/div/div[1]")
course.click()

module = username=driver.find_element(by=By.CLASS_NAME, value="modules")
module.click()