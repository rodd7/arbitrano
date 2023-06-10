from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import ElementClickInterceptedException

import time

#########################  WEBDRIVER SOURCE  #########################
CHROME_PATH = "C:\Program Files\chromedriver_win32\chromedriver.exe"
# CHROME_PATH = "/usr/local/bin/chromedriver" #mac version
######################################################################


def main():
    initDriver = Service(CHROME_PATH)
    global driver

    data = {}
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

    for x in range(len(tournamentLists)):
        try:
            if x > 0:
                driver.execute_script(f"window.scrollTo({0}, {0})")
                wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "body")))
                time.sleep(1)
                driver.find_element(
                    By.CSS_SELECTOR, "button[data-test='sportsSportsMain2TabButton']"
                ).click()

            # driver.execute_script(f"window.scrollTo({0}, {scrollLevel})")
            driver.execute_script(f"window.scrollTo({0}, {scrollLevel})")
            tournamentLists = driver.find_elements(
                By.CSS_SELECTOR, "a.f147sodr.f73eam3.f17kgnnr.f4ru8xs.f1rtv67w"
            )
            time.sleep(2)
            actions.move_to_element(tournamentLists[x]).perform()
            # wait.until(
            #     EC.element_to_be_clickable(
            #         (
            #             By.CSS_SELECTOR,
            #             "a.f147sodr.f73eam3.f17kgnnr.f4ru8xs.f1rtv67w:nth-of-type(%d)"
            #             % (x + 1),
            #         )
            #     )
            # )

            print(tournamentLists[x].location)

            scrollLevel += 50

            time.sleep(1)
            tournamentLists[x].click()
            time.sleep(1)
            driver.back()

            time.sleep(1)
        except Exception as e:
            print(f"the value of {x} doesn't pint")

    driver.quit()

    # wrong, need to research

    # match = namedtuple('match', ['name1', 'name2'])

    # data = match([], [])
    # data.name1.append((1, 2))
    # data.name1.extend([(3, 4), (5, 6)])

    # print(data)  # prints MyDataType(name1=[(1, 2), (3, 4), (5, 6)], name2=[])


if __name__ == "__main__":
    main()
