#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:  Analyst1981@gmail.com
# @date:    2019-3-16

import json
import re
from utils import get_page
from bs4 import BeautifulSoup

class ProxyMetaclass(type):
    def __new__(cls, name, bases, attrs):
        count = 0
        attrs['__CrawlFunc__'] = []
        for k, v in attrs.items():
            if 'crawl_' in k:
                attrs['__CrawlFunc__'].append(k)
                count += 1
        attrs['__CrawlFuncCount__'] = count
        return type.__new__(cls, name, bases, attrs)


class Crawler(object, metaclass=ProxyMetaclass):
    def get_proxies(self, callback):
        proxies = []
        for proxy in eval("self.{}()".format(callback)):
            print('成功获取到代理', proxy)
            proxies.append(proxy)
        return proxies
       
    def crawl_daili66(self, page_count=34):
        """
        获取代理66
        :param page_count: 页码
        :return: 代理
        """
        proxy=[]
        start_url = "http://www.66ip.cn/areaindex_{}/1.html"
        urls = [start_url.format(page) for page in range(1, page_count + 1)]
        for url in urls:
            print('Crawling', url)
            html = get_page(url)
            if html:
                soup = BeautifulSoup(html.decode("gbk"), 'lxml')
                trs=soup.find("div",class_="containerbox boxindex").find_all("tr")
                for tr in trs[1:]:
                    IP= tr.find_all("td")[0].get_text()
                    PORT = tr.find_all("td")[1].get_text()
                    TYPE = "http"
                    proxy.append([IP,PORT,TYPE])
        return proxy

    def crawl_ip3366(self):
        proxy=[]
        for page in range(1, 4):
            start_url = 'http://www.ip3366.net/free/?stype=1&page={}'.format(page)
            html = get_page(start_url)
            if html:
                soup = BeautifulSoup(html, 'lxml')
                trs=soup.find("div",id="container").find_all("tr")
                for tr in trs[1:]:
                    IP = tr.find_all("td")[0].get_text()
                    PORT = tr.find_all("td")[1].get_text()
                    TYPE = tr.find_all("td")[3].get_text().lower()
                    proxy.append([IP,PORT,TYPE])
        return proxy
              
    
    def crawl_kuaidaili(self):
        proxy=[]
        for i in range(1, 4):
            start_url = 'http://www.kuaidaili.com/free/inha/{}/'.format(i)
            html = get_page(start_url)
            if html:
                soup = BeautifulSoup(html, 'lxml')
                trs=soup.find("div",class_="con-body").find_all("tr")
                for tr in trs[1:]:
                    IP = tr.find_all("td")[0].get_text()
                    PORT = tr.find_all("td")[1].get_text()
                    iptype =tr.find_all("td")[3].get_text().lower()
                    proxy.append([IP,PORT,iptype])
        return proxy                    
                
    def crawl_xicidaili(self):
        proxy=[]
        for i in range(1, 3):
            start_url = 'http://www.xicidaili.com/nn/{}'.format(i)
            headers = {
                'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'Cookie':'_free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJWRjYzc5MmM1MTBiMDMzYTUzNTZjNzA4NjBhNWRjZjliBjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMUp6S2tXT3g5a0FCT01ndzlmWWZqRVJNek1WanRuUDBCbTJUN21GMTBKd3M9BjsARg%3D%3D--2a69429cb2115c6a0cc9a86e0ebe2800c0d471b3',
                'Host':'www.xicidaili.com',
                'Referer':'http://www.xicidaili.com/nn/3',
                'Upgrade-Insecure-Requests':'1',
            }
            html = get_page(start_url, options=headers)
            if html:
                soup = BeautifulSoup(html, 'lxml')
                trs=soup.find("table",id="ip_list").find_all("tr")
                for tr in trs[1:]:
                    IP = tr.find_all("td")[1].get_text()
                    PORT = tr.find_all("td")[2].get_text()
                    iptype =tr.find_all("td")[5].get_text().lower()
                    proxy.append([IP,PORT,iptype])
        return proxy
    
    def crawl_ip3366(self):
        proxy=[]
        for i in range(1, 4):
            start_url = 'http://www.ip3366.net/?stype=1&page={}'.format(i)
            html = get_page(start_url)
            if html:
                soup = BeautifulSoup(html, 'lxml')
                trs=soup.find("div",id="container").find_all("tr")
                for tr in trs[1:]:
                    IP = tr.find_all("td")[0].get_text()
                    PORT= tr.find_all("td")[1].get_text()
                    iptype =tr.find_all("td")[3].get_text()
                    proxy.append([IP,PORT,iptype])
        return proxy
    
    def crawl_iphai(self):
        proxy=[]
        for start_url in ['http://www.iphai.com/free/wg','http://www.iphai.com/free/ng','http://www.iphai.com/free/np','http://www.iphai.com/free/wp']:
            html = get_page(start_url)
            if html:
                soup = BeautifulSoup(html, 'lxml')
                trs=soup.find("div",class_="container main-container").find_all("tr")
                for tr in trs[1:]:
                    IP = tr.find_all("td")[0].get_text().replace(' ','').replace('\n','').replace('\r','')
                    PORT = tr.find_all("td")[1].get_text().replace(' ','').replace('\n','').replace('\r','')
                    iptype =tr.find_all("td")[3].get_text().replace(' ','').replace('\n','').replace('\r','').lower()
                    proxy.append([IP,PORT,iptype])
        return proxy