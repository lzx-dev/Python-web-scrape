#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 11:56:13 2022

@author: zexia
"""

import time
import requests
from lxml import etree
import pandas as pd
from bs4 import BeautifulSoup
from selenium     import webdriver
import json
import re


path = "/Users/zexia/Desktop/scrape /chromedriver"
driver = webdriver.Chrome(path)
driver.maximize_window()

driver.get('http://www.gguconsulting.com/school.html')

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

href = soup.find('a').get('href')

if href:
    headers = {
        'referer': 'http://www.gguconsulting.com/school.html',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
    }
    
    res = requests.get(href, headers=headers, timeout=180)




#driver.find_element_by_css_selector("#main > div.ggustart > div.inner > div > div:nth-child(2) > div.list-title > span.unfold").click()


#driver.find_element_by_css_selector("#main > div.performance > div.inner > div > div:nth-child(1) > div.list-title > span.unfold").click()




