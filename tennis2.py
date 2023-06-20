from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# from selenium.common.exceptions import ElementClickInterceptedException

import time
from collections import namedtuple

#########################  WEBDRIVER SOURCE  #########################
CHROME_PATH = "C:\Program Files\chromedriver_win32\chromedriver.exe"
# CHROME_PATH = "/usr/local/bin/chromedriver" #mac version
######################################################################


def main():
    initDriver = Service(CHROME_PATH)
    global driver

    data = []
    Game = namedtuple(
        "Game",
        ["tournament_name", "person1", "person1_odds", "person2", "person2_odds"],
    )
    webindex = 0

    driver = webdriver.Chrome(service=initDriver)
    actions = ActionChains(driver)

    options = webdriver.ChromeOptions()
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--ignore-ssl-errors")
    options.add_argument("--ignore-certificate-errors-spki-list")

    driver.get("https://pointsbet.com.au/sports/tennis")
    time.sleep(5)

    driver.find_element(
        By.CSS_SELECTOR, "button[data-test='sportsSportsMain2TabButton']"
    ).click()

    tournamentLists = driver.find_elements(
        By.CSS_SELECTOR, "a.f147sodr.f73eam3.f17kgnnr.f4ru8xs.f1rtv67w"
    )

    scrollLevel = 0
    wait = WebDriverWait(driver, 10)

    for x in range(3):
        try:
            if x > 0:
                driver.execute_script(f"window.scrollTo({0}, {0})")
                wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "body")))
                time.sleep(1)
                driver.find_element(
                    By.CSS_SELECTOR, "button[data-test='sportsSportsMain2TabButton']"
                ).click()
                time.sleep(1)

            driver.execute_script(f"window.scrollTo({0}, {scrollLevel})")
            tournamentLists = driver.find_elements(
                By.CSS_SELECTOR, "a.f147sodr.f73eam3.f1t66jgs.f4ru8xs.f1rtv67w"
            )
            time.sleep(2)
            actions.move_to_element(tournamentLists[x]).perform()
            # print(tournamentLists[x].location, {x})
            scrollLevel += 1.5 * tournamentLists[x].size["height"]
            time.sleep(1)
            # if "Futures" in driver.find_element(By.CSS_SELECTOR, "span.f1ybkwy0").text:
            #     continue

            tournamentLists[x].click()
            time.sleep(1)
            tournamentNames = driver.find_elements(
                By.CSS_SELECTOR, "div[class='f8xi195']"
            )
            namesOdds = driver.find_elements(By.CSS_SELECTOR, "div[class='faxe22p']")

            for y in range(len(tournamentNames)):
                tournamentName = (
                    tournamentNames[y]
                    .find_element(By.CSS_SELECTOR, "span[class='fi1dv9f fw739jz']")
                    .get_attribute("innerHTML")
                    .split("<")[0]
                )
                print(tournamentName)

            for z in range(len(namesOdds)):
                names = namesOdds[z].find_elements(
                    By.CSS_SELECTOR, "span[class='f1k9b6du']"
                )
                print(names[0].text, names[1].text)
                odds = namesOdds[z].find_elements(
                    By.CSS_SELECTOR, "span[class='fheif50']"
                )
                print(odds[0].text, odds[1].text)

                # data.append(
                #     Game(
                #         tournamentName,
                #         names[0].text,
                #         odds[0].text,
                #         names[1].text,
                #         odds[1].text,
                #     )
                # )

            time.sleep(1)
            driver.back()

        except Exception as e:
            print(f"index {x} is unclickable")

    # printMatch(data)
    driver.quit()


def printMatch(data):
    for match in data:
        print(match)


if __name__ == "__main__":
    main()
