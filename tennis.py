import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

import time
from collections import defaultdict

def main():
    # CHROME_PATH = "C:\Program Files\chromedriver_win32\chromedriver.exe"
    CHROME_PATH = "/usr/local/bin/chromedriver" #mac version
    data = defaultdict(list)

    initDriver = Service(CHROME_PATH)
    driver = webdriver.Chrome(service=initDriver)
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('--ignore-certificate-errors-spki-list')

    sportsbet(driver, data)
    # pointsbet(driver, data)
    # ladbrokes(driver, data)

    # sortedDict = dict(sorted(data.items(), key=lambda x: x[0].lower()) ) #this will sort our players
    for k, v in data.items():
        print(k, v)

    driver.quit()



def sportsbet(driver, data):
    driver.get('https://www.sportsbet.com.au/betting/tennis')
    time.sleep(3)
    #all bt click in and out for each one
    # driver.execute_script("window.history.go(-1)")
   
    # driver.find_element(By.XPATH, "/html/body/span/div/div/div[2]/div/div[3]/div/div/div[1]/div/div/div/div/div[1]/div[2]/div[2]/ul/li[1]/div/div/a/div/div[2]/span").click()
    

    players = driver.find_elements(By.CSS_SELECTOR,"span[data-automation-id*='outcome-name']")
    numbers = driver.find_elements(By.CSS_SELECTOR,"span[data-automation-id*='price-text']")
    storeData (players, numbers, data)

def pointsbet(driver, data):
    driver.get('https://pointsbet.com.au/sports/tennis')
    time.sleep(3)
    players = driver.find_elements(By.CSS_SELECTOR,"span[class='f5rl2hl']")
    numbers = driver.find_elements(By.CSS_SELECTOR,"span[class='fheif50']")
    storeData (players, numbers, data)

def ladbrokes(driver, data):
    driver.get('https://www.ladbrokes.com.au/sports/tennis')
    time.sleep(3)
    players = driver.find_elements(By.CSS_SELECTOR,"span[class='displayTitle']")
    numbers = driver.find_elements(By.CSS_SELECTOR,"div[class='price-button-odds-price']")
    storeData (players, numbers, data)

def storeData (players, numbers, data):
    for x in range(len(players)):
        data[players[x].text].append(numbers[x].text)


def highestReturn (player):
    return max(player)



# soup = BeautifulSoup(requests.get(TAB).text, "html.parser")
# player = soup.find('span', class_='participant')
# print(soup.prettify())


# https://marktheballot.blogspot.com/2018/06/the-dramas-of-daily-web-scraper.html

if __name__ == "__main__":
    main()