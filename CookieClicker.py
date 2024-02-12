import requests
from bs4 import BeautifulSoup
import selenium
from selenium.webdriver.common.by import By

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager
import time
options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

url = "https://orteil.dashnet.org/cookieclicker/"

driver.get(url)

time.sleep(2)
consent_button = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[1]/div[2]/div[2]/button[1]")
consent_button.click()

time.sleep(2)
english = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[12]/div/div[1]/div[1]/div[2]")
english.click()

time.sleep(5)
cepums = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[15]/div[8]/button")

source = driver.page_source
soup = BeautifulSoup(source, "html.parser")
item = soup.find(id="cookies").text
d = item.split(" ")
daudz = int(d[0])
spiedeji = int(soup.find(id="productPrice0").text)


if daudz > spiedeji :
    spiedejs = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[19]/div[3]/div[6]/div[2]")
    spiedejs.click()

else :
    for x in range(1, 100):
        
        cepums.click()

        item = soup.find(id="cookies").text
        d = item.split(" ")
        source = driver.page_source
        soup = BeautifulSoup(source, "html.parser")
        daudz = int(d[0])
        spiedeji = int(soup.find(id="productPrice0").text)
    
   



time.sleep(400)
driver.quit()
