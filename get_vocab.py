import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


from selenium.webdriver.support.ui import Select
import re
from time import sleep
import os

import ssl

ssl._create_default_https_context = ssl._create_unverified_context



driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://www.wlangames.net/hwenchinese3.php")
driver.find_element(By.XPATH, '//*[@id="TheForm"]/font/table[3]/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr[7]/td/label').click()

#driver.execute_script("gotoVocabularyList();")


#obtain parent window handle
p = driver.window_handles[0]
#obtain browser tab window
c = driver.window_handles[1]
#switch to tab browser
driver.switch_to.window(c)

html_source = driver.page_source

try:
    os.remove('vocab_list.html')
except: 
    pass

with open("vocab_list.html", "w") as f:
    f.write(html_source)




