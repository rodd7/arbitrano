from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


import time
from collections import defaultdict
import json

CHROME_PATH = "C:\Program Files\chromedriver_win32\chromedriver.exe"
# CHROME_PATH = "/usr/local/bin/chromedriver" #mac version

URLSize = 0
URLCount = -1

def main():
    data = defaultdict(list)
    initDriver = Service(CHROME_PATH)
    

    global driver

    driver = webdriver.Chrome(service = initDriver)
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('--ignore-certificate-errors-spki-list')

    file = open('arbitrano.json')
    arbitrano = json.load(file)
    setURLSize(len(arbitrano['betters']))
    for better in arbitrano['betters']:
        initialScrape(better['URL'], better['playerSelector'], better['oddSelector'], data)
        # if (better['URL'] == 'https://pointsbet.com.au/sports/tennis'):
        #     driver.find_element(By.CSS_SELECTOR,"button[data-test='sportsSportsMain3TabButton']").click()
        #     time.sleep(2)
        #     for element in driver.find_elements(By.CSS_SELECTOR,"div[class='f2nndsr f1d8xtm1']"):
        #         test = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div[class='f2nndsr f1d8xtm1']")))
        #         test.click()
        #         element.click()
        #         time.sleep(1)
        #         driver.back()
        #         driver.find_element(By.CSS_SELECTOR,"button[data-test='sportsSportsMain3TabButton']").click()
            

    # print(data)
    count = 0
    for k, v in data.items():
        count+=1
        print(k, v)
        print(count)

    driver.quit()

def setURLSize(x):
    global URLSize
    URLSize = x

def setURLCount():
    global URLCount
    URLCount+=1

def initialScrape(URL, playerSelector, oddSelector, data):
    driver.get(URL)
    time.sleep(3)
    setURLCount()
    initStore(driver.find_elements(By.CSS_SELECTOR,playerSelector), driver.find_elements(By.CSS_SELECTOR,oddSelector), data)

def initStore(players, numbers, data):
    for x in range(len(players)):
        if not data[players[x].text]:
            data[players[x].text] = ['0.00'] * URLSize

        for y in range(len(data[players[x].text])):
            if y == URLCount:
                data[players[x].text][y] = numbers[x].text

# def initStore(players, numbers, data):
#     print(URLSize)
#     for x in range(len(players)):
#         data[players[x].text].append(numbers[x].text)


# https://marktheballot.blogspot.com/2018/06/the-dramas-of-daily-web-scraper.html

if __name__ == "__main__":
    main()