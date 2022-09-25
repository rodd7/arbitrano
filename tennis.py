import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from collections import defaultdict

def main():
    CHROME_PATH = "C:\Program Files\chromedriver_win32\chromedriver.exe"

    SPORTSBET = "https://www.sportsbet.com.au/betting/tennis" # POSITION 0
    TAB = "https://www.tab.com.au/sports/betting/Tennis" # POSITION 1 CURRENTLY DIFFICULT TO DO
    POINTSBET = "https://pointsbet.com.au/sports/tennis/" # POSITION 2

    weblist = [SPORTSBET, TAB, POINTSBET]
    data = defaultdict(list)


    driver = webdriver.Chrome(executable_path=CHROME_PATH)
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('--ignore-certificate-errors-spki-list')

    driver.get(SPORTSBET)
    players = driver.find_elements_by_css_selector("span[data-automation-id*='outcome-name']")
    numbers = driver.find_elements_by_css_selector("span[data-automation-id*='price-text']")
    
            
    for x in range(len(players)):
        data[players[x].text] = [numbers[x].text]
        

    driver.get(POINTSBET)
    time.sleep(3)

    players = driver.find_elements_by_css_selector("span[class='f5rl2hl']")
    numbers = driver.find_elements_by_css_selector("span[class='fheif50']")

    for x in range(len(players)):
        data[players[x].text].append(numbers[x].text)


    print(data)


    driver.quit()



def sportsbet():
    return

def highestReturn (player):
    return max(player)





# soup = BeautifulSoup(requests.get(TAB).text, "html.parser")
# player = soup.find('span', class_='participant')
# print(soup.prettify())


# https://marktheballot.blogspot.com/2018/06/the-dramas-of-daily-web-scraper.html

if __name__ == "__main__":
    main()