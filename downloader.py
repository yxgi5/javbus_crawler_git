#!/usr/bin/env python
#-*-coding:utf-8-*-

import requests
import urllib.request
from bs4 import BeautifulSoup

proxy_addr = "127.0.0.1:8118"

# headers = {
#     'User-Agent	' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0', 
# }

def get_html(url, Referer_url=None):
    '''get_html(url),download and return html'''
    # if Referer_url:
    #     headers['Referer'] = Referer_url
    # req = requests.get(url, headers=headers)
    # return req.content

    if Referer_url==None:
        Referer_url = url

    proxy = urllib.request.ProxyHandler({'https': proxy_addr})
    opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
    opener.addheaders = [
        ('authority', 'www.javbus.com'),
        ('accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'),
        ('accept-language', 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7'),
        ('cache-control', 'max-age=0'),
        # ('cookie', 'PHPSESSID=771k7892n521mh0o3ncebeohj6; existmag=mag; 4fJN_2132_seccodecSlqvwSe=27300.4c48839aa773245d55; age=verified; dv=1'),
        ('cookie', '4fJN_2132_seccodecSeRRfg5=14339.4cce2e4f1ae59e531e; 4fJN_2132_seccodecSTVfEvf=9372.f1ae0a808eec67ca6a; 4fJN_2132_seccodecSXYwYAC=20246.0620c823cb43b800c7; 4fJN_2132_seccodecSM7ir7C=32974.501fed7ed7e50412ed; 4fJN_2132_seccodecSQTZPiM=26549.061809068ea08ce4ce; PHPSESSID=9ku0thftv26h49i683n1ml0ag1; existmag=mag; dv=1'),
        ('Referer',Referer_url),
        ('sec-ch-ua', 'sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="104", "Opera";v="90"'),
        ('sec-ch-ua-mobile', '?0'),
        ('sec-ch-ua-platform', '"Linux"'),
        ('sec-fetch-dest', 'document'),
        ('sec-fetch-mode', 'navigate'),
        ('sec-fetch-site', 'same-origin'),
        ('sec-fetch-user', '?1'),
        ('upgrade-insecure-requests', '1'),
        ('User-Agent',
         'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84'),
        ('X-Requested-With','XMLHttpRequest')
    ]
    urllib.request.install_opener(opener)

    for i in range(5):
        try:
            soup = BeautifulSoup(urllib.request.urlopen(url).read().decode('utf-8', errors='ignore'), 'lxml')
            break
        # except Exception as ret:
        #     raise Exception(ret)
        #     # print(ret)
        # except IncompleteRead:
        except Exception as err:
            print(err)
            if i == 4:
               raise     # give up after 5 attempts

    html = soup.prettify()
    return html