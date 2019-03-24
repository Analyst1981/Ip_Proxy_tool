#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:  Analyst1981@gmail.com
# @date:    2019-3-16


import requests
from bs4 import BeautifulSoup
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
}
def get_proxy():
    r = requests.get('http://127.0.0.1:5555/random')
    soup = BeautifulSoup(r.text, "lxml")
    trs=soup.find("div",id="container").find_all("tr")
    for tr in trs[1:]:
        IP = tr.find_all("td")[0].get_text()
        PORT = tr.find_all("td")[1].get_text()
    proxies = {
        'http': 'http://' +IP+":"+PORT,
        'https': 'https://' +IP+":"+PORT
    }    
    return proxies


def crawl(url, proxy):
    print(proxy)
    r = requests.get(url,headers=headers, proxies=proxy,verify=False)
    if response.status_code == 200:
    print('Successfully')
    print(response.text)
    return r.text


def main():
    while True:
        for url in ['https://api.ipify.org?format=json','http://www.whatismyip.com']:
            try:
                proxy = get_proxy()
                html = crawl(url, proxy)
                print(html)
            except:
                pass
        continue

if __name__ == '__main__':
    main()

