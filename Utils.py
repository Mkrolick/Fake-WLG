
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

from logging import captureWarnings
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import re
from time import sleep


def Generate_Vocab_Tuple():
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
        

    # html from the vocab page
    html = open('vocab_list.html', 'r')

    # creates a regular expression pattern to detect a starting place
    # where a later patter will run and not return an error
    pattern = re.compile(r'\<table cellpadding="1"\>(.*)', re.DOTALL)

    # Creates Matches
    matches = pattern.finditer(html.read())

    # iterates through matches. Selects the first group. Returns a string representation
    innerHTMLMinusTbody = [match for match in matches][0].group(1)



    #pattern to detect differnt table rows based on script and info pattern
    pattern = re.compile(r'\<script\>\ninfo\[.*?\] = new Array\(\);\n(.*?)\<\/script\>', re.DOTALL)


    #matches pattern
    matches = pattern.finditer(innerHTMLMinusTbody)


    language_tuple_list = []

    # creates index variable for testing
    #i = 0

    # iterates through matches
    for match in matches:


        # turns match element into a readable string
        table_element = match.group(1)

        # creates a regular expression vocab pattern for character recognition
        vocab_symbol_patterns = re.compile(r'info\[.*?\]\[2\] = \"(.*?)\";', re.DOTALL)

        # creates a regular expression vocab pattern for pinyin string recognition
        vocab_pinyin_patterns = re.compile(r'info\[.*?\]\[3\] = \"(.*?)\";', re.DOTALL)

        # creates a regular expression vocab pattern for english string recognition
        vocab_english_patterns = re.compile(r'info\[.*?\]\[4\] = \"(.*?)\";', re.DOTALL)


        #Creates a class storing engish, pinyin, character values
        temp_vocab = (vocab_symbol_patterns.findall(table_element)[0], vocab_pinyin_patterns.findall(table_element)[0], vocab_english_patterns.findall(table_element)[0])

        #Appends class to the language tuple string
        language_tuple_list.append(temp_vocab)

        #tempory bug fix indexer
        #i += 1

        





