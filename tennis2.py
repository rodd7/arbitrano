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
from collections import defaultdict
import collections
import json
from arbitrage import *


CHROME_PATH = "C:\Program Files\chromedriver_win32\chromedriver.exe"
# CHROME_PATH = "/usr/local/bin/chromedriver" #mac version

def main():
    print("test")

if __name__ == "__main__":
    main()