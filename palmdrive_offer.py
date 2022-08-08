#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 16:42:18 2022

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

driver.get('http://www.palmdrive.cn/v2/graduate.html#/offers')

driver.find_element_by_css_selector("#app > div > div.home > div > div.banner3-div > div.demos-div > div.more-demos > div:nth-child(1)").click()
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

offer_list = []
for offer in soup.find_all("div", class_ = "each-demo"):
    offer_dic = {}
    offer_dic["admission_school"] = offer.find("div", class_ = "demo-admissionSchool").text
    offer_dic["admission_major"] = offer.find("div", class_ = "demo-admissionMajor").text
    offer_dic["undergraduate"] = offer.find("div", class_ = "demo-text line1").text
    offer_dic["background"] = offer.find("div", class_ = "demo-text line3").text
    offer_list.append(offer_dic)
    
    

data  = {}
data["offer_info"] = offer_list

with open('/Users/zexia/Desktop/proDream scrpae/palmdrive_offer.json', "w") as fp:
    json.dump(data, fp, ensure_ascii = False)




    
    
    
    
    
    
    
    