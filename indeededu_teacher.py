#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 13:19:36 2022

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
driver.get('https://indeededu.com/about-us/')


html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

teacher_list = []

sections = soup.find_all("section")

#teacher section range
#8 - 46

for i in range(7, 47, 2):

    teacher_dic = {}
    teacher_dic["teacher_name"] = sections[i].h3.text
    if sections[i].find("div", class_="team-member-description"):
        teacher_dic["title"] = sections[i].find("div", class_="team-member-description").text
    elif sections[i].b:
        teacher_dic["title"] = sections[i].b.text
    else: 
        teacher_dic["title"] = "None"
        
    teacher_dic["intro"] = sections[i + 1].p.text      
    teacher_list.append(teacher_dic)
   
data  = {}
data["info"] = teacher_list

with open('/Users/zexia/Desktop/proDream scrpae/indeededu_teacher.json', "w") as fp:
    json.dump(data, fp, ensure_ascii = False)
        
        
    






