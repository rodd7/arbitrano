from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from selenium.common.exceptions import TimeoutException


import time
from collections import defaultdict
import collections
import json
from arbitrage import *

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
        #     driver.find_element(By.CSS_SELECTOR,"button[data-test='sportsSportsMain1TabButton']").click()
        #     additionalScrape(better['playerSelector'], better['oddSelector'], data)

        # need to reapproach ^^ messing everything up



            # numEvents = driver.find_element(By.CSS_SELECTOR,"div[identifier='sports_default_sports-all-comps'").find_elements(By.CSS_SELECTOR,"div[class='f2nndsr f1d8xtm1']")

            # for element in range(0, len(numEvents)):
            #     test = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div[class='f2nndsr f1d8xtm1']")))
            #     print(element)
            #     # while True:
            #     #     try:
            #     #         if element == 0:
            #     #             test = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//*[@id=\"mainContent\"]/div[1]/div/div[2]/div/div/div/div[3]/div/section[1]/div/div/a/div/div[2]")))
            #     #         else:
            #     #             test = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//*[@id=\"mainContent\"]/div[1]/div/div[2]/div/div/div/div[3]/div/section[2]/div/div/a[" + str(element) + "]/div/div[2]")))
            #     #     except TimeoutException:
            #     #         newSection+=1
            #     #         continue
            #     #     break

            #     numEvents[element].click()
            #     time.sleep(1)
            #     driver.back()
            #     driver.find_element(By.CSS_SELECTOR,"button[data-test='sportsSportsMain2TabButton']").click()

# {
# 			"better": "Bet365",
# 			"URL": "https://www.bet365.com.au/#/AC/B13/C1/D50/E2/F163/",
# 			"playerSelector": "div[class='rcl-ParticipantFixtureDetailsTeam_TeamName']",
# 			"oddSelector": "span[data-testid='price-button-odds']"
# 		}



    # print(data)
    count = 0
    for k, v in data.items():
        count+=1
        print(count, "= ", k, v)
    
    scanDuplicates(data)
    

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
    store(driver.find_elements(By.CSS_SELECTOR,playerSelector), driver.find_elements(By.CSS_SELECTOR,oddSelector), data)

def additionalScrape(playerSelector, oddSelector, data):
    time.sleep(3)
    store(driver.find_elements(By.CSS_SELECTOR,playerSelector), driver.find_elements(By.CSS_SELECTOR,oddSelector), data)

# def store(players, numbers, data):
#     for x in range(len(players)):
#         if not data[players[x].text]:
#             data[players[x].text] = ['0.00'] * URLSize

#         for y in range(len(data[players[x].text])):
#             if y == URLCount:
#                 data[players[x].text][y] = numbers[x].text

def store(players, numbers, data):
    for x in range(len(players)):
        uppercase = str(players[x].text).upper()
        if not data[uppercase]:
            data[uppercase] = ['0.00'] * URLSize

        for y in range(len(uppercase)):
            if y == URLCount:
                data[uppercase][y] = numbers[x].text

# def initStore(players, numbers, data):
#     print(URLSize)
#     for x in range(len(players)):
#         data[players[x].text].append(numbers[x].text)

def scanDuplicates(data):
    names = []
    for players in data:
        name = str(players).split()
        names.append(name[-1])
    
    print([item for item, count in collections.Counter(names).items() if count > 1])

    # if no '/' in key value
    # if first name is one letter and letter of name[0] == first letter of name[-1], merge

def firstnameCheck(player, data):
    player = str(player).split()
    first = player[0]
    last = player[-1]

    if len(first) > 1:
        return 0

    for player in data:
        target = str(player).split()
        targetFirst = target[0]
        targetLast = target[-1]
        if targetFirst == first and targetLast == last:
            return 1

# https://marktheballot.blogspot.com/2018/06/the-dramas-of-daily-web-scraper.html

if __name__ == "__main__":
    main()