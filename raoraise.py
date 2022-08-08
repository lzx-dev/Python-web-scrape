#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 15:15:59 2022

@author: zexia
"""


import requests
from lxml import etree
from bs4 import BeautifulSoup
from selenium     import webdriver
import json
import re



path = "/Users/zexia/Desktop/scrape /chromedriver"
driver = webdriver.Chrome(path)
driver.maximize_window()
teacher_list = [] 


for i in range(29, 40):
    driver.get('http://www.taoraise.com/teacher/pid_30_sort_1_page_' + str(i) + "/")
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    div_list = soup.find("div", class_ = "school_list_l teacher_list_l").find_all("div", class_ = "pic")
   
    for div in div_list:
        href = div.find('a').get('href')
        number = re.search("-(.*).html", href).group(1)


        cookies = {
            'Hm_lvt_03f4fb49b90bd153785521d20e15db54': '1658274157',
            'Hm_lpvt_03f4fb49b90bd153785521d20e15db54': '1658274157',
            }
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            
            'Pragma': 'no-cache',
            'Referer': 'http://www.taoraise.com/teacher/detail-' + str(number) + ".html",
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
            }
        url = 'http://www.taoraise.com/teacher/detail_teacher-' + str(number) + ".html"
        response = requests.get(url, cookies=cookies, headers=headers, verify=False, timeout = 20)
        bs = BeautifulSoup(response.text, 'lxml')
        dd_list = bs.find_all('dd')
        teacher_dict = {}
        for dd in dd_list:
            text = dd.text
            key = text.split('：')[0]
            value = text.split('：')[1]
            teacher_dict[key] = value

        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
            }
    
        res = requests.get(href, headers=headers, timeout=180)
        html_l = etree.HTML(res.text)
        teacher_dict["姓名"] =  ''.join(html_l.xpath("/html/body/div[11]/div/div[2]/h4/text()")).replace("\r\n", "").replace("  ", "")        
        teacher_dict["地址"] = "".join(html_l.xpath("/html/body/div[11]/div/div[2]/h4/span/text()"))
        teacher_dict["费用"] =  ''.join(html_l.xpath("/html/body/div[11]/div/div[2]/div[1]/dl/dd[4]/font/text()")).replace("\r\n", "").replace("  ", "")
        teacher_dict["介绍"] =  html_l.xpath("/html/body/div[11]/div/div[2]/div[2]/text()[1]")[0].replace("\r\n", "").replace("  ", "")
        
        
        teacher_list.append(teacher_dict)
        
        


data  = {}
data["info"] = teacher_list


with open('/Users/zexia/Desktop/proDream scrpae/raoraise_2.json', "w") as fp:
    json.dump(data, fp, ensure_ascii = False)




    
    
   
    
    

