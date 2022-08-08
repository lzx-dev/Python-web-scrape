#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 14:56:50 2022

@author: zexia
"""

import requests
from lxml import etree
from bs4 import BeautifulSoup
from selenium     import webdriver
import json
import re
from selenium.webdriver.common.by import By



path = "

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
            'Referer': path,
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
            }

response = requests.get(path, cookies=cookies, headers=headers, verify=False, timeout = 20)
bs = BeautifulSoup(response.text, 'lxml')





for i in range(1,2):
    try:

        offer_list = []
        div_list = bs.find("div", class_ = "case_list").find_all("div", class_ = "item")


        for offer in div_list:
            offer_dict = {}
            for info in offer.find_all("p"):
                text = info.text
                key = text.split('：')[0]
                value = text.split('：')[1]
                offer_dict[key] = value
                offer_list.append(offer_dict)
                
            
        
   
    except:
        print("error")
        pass















