from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

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


    

    print(data)
    
    # for k, v in data.items():
    #     print(k, v)

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
    print(URLSize)
    for x in range(len(players)):
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