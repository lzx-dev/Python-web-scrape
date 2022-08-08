#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 22:39:50 2022

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
driver.get('https://nlg.cheersyou.com/cases')






#headers = {
#        'referer': 'https://nlg.cheersyou.com/cases',
#        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
#    }

total_page = 14

##展开所有案例
for i in range(1, total_page + 1):
    try:
        print('正在滑动第{}页完成了'.format(i))
        driver.find_element_by_css_selector("#content-data-list > div > div > ul > li > a").click()
        driver.implicitly_wait(15)
        time.sleep(1.5)
    except Exception as e:
        print(e)
        print('第', i,'页点击失败，可能没有滑到位，跳过次循环')
        time.sleep(10)
        continue

##获取html
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
student_list = []



##逐条获取信息： 成绩 获取offer
student_info = soup.find_all('div', class_ = "col-xs-12 col-sm-3")
for student in student_info:
    student_dic = {}
    student_text = student.find("div", class_ = "action-bg-info").text
    
    
    
    if "GRE" in student_text and "GPA" not in student_text:
        student_dic["毕业于"] = re.search('毕业于：(.*)', student_text).group(1).replace("\xa0", "")
        student_dic["GRE"] = re.search('GRE: (.*)', student_text).group(1).replace("\xa0", "")
    elif "GRE" in student_text and "GPA" in student_text:
        student_dic["毕业于"] = re.search('毕业于：(.*)', student_text).group(1).replace("\xa0", "")
        student_dic["GPA"] = re.search('GPA: (.*) \|\ GRE', student_text).group(1).replace("\xa0", "")
        student_dic["GRE"] = re.search('GRE: (.*)', student_text).group(1).replace("\xa0", "")
    elif "SSAT" in student_text:
        student_dic["毕业于"] = re.search('毕业于：(.*)', student_text).group(1).replace("\xa0", "")
        student_dic["SSAT"] = re.search('SSAT: (.*)', student_text).group(1).replace("\xa0", "")
    elif "GPA" in student_text:
        student_dic["毕业于"] = re.search('毕业于：(.*)', student_text).group(1).replace("\xa0", "")
        student_dic["GPA"] = re.search('GPA: (.*)', student_text).group(1).replace("\xa0", "")

    offer = []
    for i in student.find_all("div", class_ = "field-item"):
        offer.append(i.text.replace("\n", ""))
    student_dic["offer"] = offer
    
    student_list.append(student_dic)
   
data  = {}
data["info"] = student_list

print(data)
with open('/Users/zexia/Desktop/proDream scrpae/cheersyou.json', "w") as fp:
    json.dump(data, fp, ensure_ascii = False)
        


#res = requests.get(href, headers=headers, timeout=180)


