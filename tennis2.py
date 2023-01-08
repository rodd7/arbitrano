#this version is going to be improved
#everything has to be re-approached because some websites have different configurations and making them similar will break and be harder
#don't use defaultdict, be creative

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from selenium.common.exceptions import TimeoutException

import time
from collections import namedtuple
from arbitrage import *

#########################  WEBDRIVER SOURCE  #########################
CHROME_PATH = "C:\Program Files\chromedriver_win32\chromedriver.exe"
# CHROME_PATH = "/usr/local/bin/chromedriver" #mac version
######################################################################

def main():

    initDriver = Service(CHROME_PATH)
    global driver

    data = {}

    driver = webdriver.Chrome(service = initDriver)
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('--ignore-certificate-errors-spki-list')

    driver.get('https://pointsbet.com.au/sports/tennis')
    players = driver.find_elements(By.CSS_SELECTOR,"span[class='f5rl2hl']")
    numbers = driver.find_elements(By.CSS_SELECTOR,"span[class='fheif50']")

    for x in range(len(players)):
        print()
    #time.sleep(3)

    driver.quit()

    
    # wrong, need to research

    # match = namedtuple('match', ['name1', 'name2'])

    # data = match([], [])
    # data.name1.append((1, 2))
    # data.name1.extend([(3, 4), (5, 6)])

    # print(data)  # prints MyDataType(name1=[(1, 2), (3, 4), (5, 6)], name2=[])



if __name__ == "__main__":
    main()