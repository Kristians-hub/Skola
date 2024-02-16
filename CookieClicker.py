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

time.sleep(1)
consent_button = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[1]/div[2]/div[2]/button[1]")
consent_button.click()

time.sleep(1.5)
english = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[12]/div/div[1]/div[1]/div[2]")
english.click()

time.sleep(1)
cepums = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[15]/div[8]/button")

source = driver.page_source
soup = BeautifulSoup(source, "html.parser")



spiedeji = int(soup.find(id="productPrice0").text)

def cepuma_daudz():
    source = driver.page_source
    soup = BeautifulSoup(source, "html.parser")
    item = soup.find(id="cookies").text
    d = item.split(" ")
    daudz = int(d[0])
    return daudz
for x in range(1, 150):
     cepums.click()

spiedejs = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[19]/div[3]/div[6]/div[2]")
spiedejs.click()
clikers = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[19]/div[3]/div[5]/div[1]")
clikers.click()

for x in range(1, 100000):

        cepums.click()
        daudz = cepuma_daudz()
        spiedeji = int(soup.find(id="productPrice0").text)
        vecmams = int(soup.find(id="productPrice1").text)
     
        if daudz > spiedeji:
            spiedejs = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[19]/div[3]/div[6]/div[2]")
            spiedejs.click()

            cepums = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[15]/div[8]/button")
            source = driver.page_source
            soup = BeautifulSoup(source, "html.parser")
            spiedeji = int(soup.find(id="productPrice0").text)
        elif daudz > vecmams:
             vecmama = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[19]/div[3]/div[6]/div[3]")
             vecmama.click()

        
           






spiedejs = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[19]/div[3]/div[6]/div[2]")
spiedejs.click()





time.sleep(400000)
driver.quit()

#/html/body/div[3]/div[2]/div[1]/div[2]/div[2]/button[1]
