#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 10:54:32 2022

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

driver.get('http://www.gguconsulting.com/team.html')


teacher_list = []
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')


people = soup.find_all("div", class_= "clear")

for teacher in people:
    try:
        teacher_dic = {}
        teacher_dic["name"] = teacher.find("div", class_= "message").h3.text
        teacher_dic["title"] = teacher.find("div", class_= "message").h4.text
        teacher_dic["intro"] = teacher.p.text
        teacher_list.append(teacher_dic)
    except:
        pass

data  = {}
data["teacher_info"] = teacher_list 



with open('/Users/zexia/Desktop/proDream scrpae/ggu_teacher.json', "w") as fp:
    json.dump(data, fp, ensure_ascii = False)





