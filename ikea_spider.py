# -*- coding: utf-8 -*-
# ☯ Date  : 2021/11/22 20:00
import time
import requests
from lxml import etree
import pandas as pd
from bs4 import BeautifulSoup
from selenium     import webdriver


def get_data_drvier():
    
    path = "/Users/zexia/Desktop/project/chromedriver"
    driver = webdriver.Chrome(path)
    driver.maximize_window()
    # driver.set_window_size(1920, 1080)
    # selenium请求目标网站
    # q=sofa  总8页
    # q=Chair  总7页
    # q=table  总4页
    # q = bedframe 总4页
    data_list = [['sofa', 8], ['Chair', 7], ['table', 4], ['bedframe',4], ['light', 4] ]
    for product, total_page in data_list:
        driver.get('https://www.ikea.com/us/en/search/products/?q={}'.format(product))
        driver.implicitly_wait(30)
        time.sleep(3)

        # total_page = 8
        for i in range(1, total_page + 1):
            try:
                
                

                i = i*96
                print('正在滑动第{}页完成了'.format(i))

                target = driver.find_element_by_css_selector('#search-results > div:nth-child({}) > div.range-revamp-product-compact__bottom-wrapper > a > div > div.range-revamp-compact-price-package__additional-info > h3 > span.range-revamp-header-section__title--small.notranslate'.format(i+1))
                time.sleep(1.5)
                driver.execute_script("arguments[0].scrollIntoView();", target)
                time.sleep(5)
                driver.find_element_by_xpath("//div[@class='show-more']/a[@class='show-more__button button button--secondary button--small']/span").click()
                driver.implicitly_wait(30)
                time.sleep(1.5)
            except Exception as e:
                print(e)
                print('第', i,'页点击失败，可能没有滑到位，跳过次循环')
                time.sleep(10)
                continue



        time.sleep(3)

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        result_list = soup.find('div', id='search-results').find_all("div", class_="product-fragment serp-grid__item serp-grid__item--product search-grid__item range-revamp-product-compact product-fragment")

        conl_href = []
        for div in result_list:

            href = div.find('a').get('href')
            if href:
                conl_href.append(href)

        get_href(conl_href, product)
    driver.close()


# 获取商品详情数据
def get_href(conl_href, product):

    conlist = list()
    headers = {
        'referer': 'https://www.ikea.com/us/en/search/products/?q={}'.format(product),
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
    }
    for href in conl_href:
        try:
            # 用request 发送每个href请求响应
            res = requests.get(href, headers=headers, timeout=180)

            html_l = etree.HTML(res.text)
            item = dict()
            # 获取 产品详情
            product_details = ''.join(html_l.xpath("//div[@class='range-revamp-product-details__container']/span[@class='range-revamp-product-details__paragraph']//text()"))
            # 获取 评论数
            number_comments = ''.join(html_l.xpath("//div[@class='js-price-package range-revamp-pip-price-package']/button[@class='range-revamp-average-rating range-revamp-average-rating__button']/span[@class='range-revamp-average-rating__details']/span[@class='range-revamp-average-rating__reviews']/text()")).replace('(', '').replace(')', '')
            # 获取 评分
            score = ''.join(html_l.xpath("//span[@class='range-revamp-average-rating__header']/text()"))
            item['score'] = score
            item['number_comments'] = number_comments
            item['product_details'] = product_details
            print(href)
            print(item)
            conlist.append(item)
            csv_to(conlist, product)
        except Exception as e:
            print(e)
            print(href, '此链接访问失败，跳过此链接')
            time.sleep(10)
            continue


# 存储数据
def csv_to(content_l, product):
    pd.DataFrame(content_l).to_csv('ikea_data_{}.csv'.format(product), encoding='utf-8-sig')


get_data_drvier()