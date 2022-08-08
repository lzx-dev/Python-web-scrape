#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 15:45:39 2022

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

driver.get('http://www.palmdrive.cn/v2/graduate.html#/teachers')


##展开所有老师
driver.find_element_by_css_selector("#app > div > div.teacher-intro > div.web-div > div.banner5-div > div.teachers-div > div.more-teachers > div:nth-child(1)").click()
teacher_list = []
total_teacher = 24

#24

for i in range(1, total_teacher + 1):
    try:
        teacher_dic = {}
        driver.find_element_by_css_selector("#app > div > div.teacher-intro > div.web-div > div.banner5-div > div.teachers-div > div:nth-child" + "(" + str(i) + ")").click()
    
    #headers = {
    #    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
    #}
    
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        for title, school in zip(soup.find("div", class_ = "teacher-div").find_all("div", class_ = "title"),   
                                 soup.find("div", class_ = "teacher-div").find_all("div", class_ = "school")):
            teacher_dic[title.text] = school.text
        
        for section, detail in zip(soup.find_all("span", class_ = "each-section"), 
                                   soup.find_all("div", class_ = "each-section-detail")):
            teacher_dic[section.text] = detail.text
            
        teacher_list.append(teacher_dic)
        time.sleep(15)
    

        driver.find_element_by_css_selector("#app > div > div.teacher-intro > div.teacherInfoDialog > div > div > div.el-dialog__header > button").click()
        time.sleep(15)
    except:
        pass

    
    
data  = {}
data["teacher_info"] = teacher_list 
with open('/Users/zexia/Desktop/proDream scrpae/palmdrive.json', "w") as fp:
    json.dump(data, fp, ensure_ascii = False)
    
    
                                    
    

    
 

