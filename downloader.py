#!/usr/bin/env python
#-*-coding:utf-8-*-

import requests
# import urllib.request
from bs4 import BeautifulSoup
from http.client import IncompleteRead
import time

# proxy_addr = "127.0.0.1:8118"

# headers = {
#     'User-Agent	' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0', 
# }
# def get_html(url, Referer_url=None):
#     '''get_html(url),download and return html'''
#     if Referer_url:
#         headers['Referer'] = Referer_url
#     req = requests.get(url, headers=headers)
#     return req.content

# def get_html(url, Referer_url=None):
#     '''get_html(url),download and return html'''
#     # if Referer_url:
#     #     headers['Referer'] = Referer_url
#     # req = requests.get(url, headers=headers)
#     # return req.content

#     if Referer_url==None:
#         Referer_url = url

#     proxy = urllib.request.ProxyHandler({'https': proxy_addr})
#     opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
#     opener.addheaders = [
#         ('authority', 'www.javbus.com'),
#         ('accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'),
#         ('accept-language', 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7'),
#         ('cache-control', 'max-age=0'),
#         # ('cookie', 'PHPSESSID=771k7892n521mh0o3ncebeohj6; existmag=mag; 4fJN_2132_seccodecSlqvwSe=27300.4c48839aa773245d55; age=verified; dv=1'),
#         ('cookie', '4fJN_2132_seccodecSeRRfg5=14339.4cce2e4f1ae59e531e; 4fJN_2132_seccodecSTVfEvf=9372.f1ae0a808eec67ca6a; 4fJN_2132_seccodecSXYwYAC=20246.0620c823cb43b800c7; 4fJN_2132_seccodecSM7ir7C=32974.501fed7ed7e50412ed; 4fJN_2132_seccodecSQTZPiM=26549.061809068ea08ce4ce; PHPSESSID=9ku0thftv26h49i683n1ml0ag1; existmag=mag; dv=1'),
#         ('Referer',Referer_url),
#         ('sec-ch-ua', 'sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="104", "Opera";v="90"'),
#         ('sec-ch-ua-mobile', '?0'),
#         ('sec-ch-ua-platform', '"Linux"'),
#         ('sec-fetch-dest', 'document'),
#         ('sec-fetch-mode', 'navigate'),
#         ('sec-fetch-site', 'same-origin'),
#         ('sec-fetch-user', '?1'),
#         ('upgrade-insecure-requests', '1'),
#         ('User-Agent',
#          'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84'),
#         ('X-Requested-With','XMLHttpRequest')
#     ]
#     urllib.request.install_opener(opener)

#     for i in range(5):
#         try:
#             soup = BeautifulSoup(urllib.request.urlopen(url).read().decode('utf-8', errors='ignore'), 'lxml')
#             break
#         # except Exception as ret:
#         #     raise Exception(ret)
#         #     # print(ret)
#         # except IncompleteRead:
#         except Exception as err:
#             print(err)
#             if i == 4:
#                raise     # give up after 5 attempts

#     html = soup.prettify()
#     return html

# def get_html(url, Referer_url=None, unsafe=False, max_retries=5):
#     '''get_html(url),download and return html'''
#     # if Referer_url:
#     #     headers['Referer'] = Referer_url
#     # req = requests.get(url, headers=headers)
#     # return req.content

#     bytes_ranges_supported = False
#     html_raw = b''

#     if Referer_url==None:
#         Referer_url = url

#     proxy = urllib.request.ProxyHandler({'https': proxy_addr})
#     opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
#     opener.addheaders = [
#         ('authority', 'www.javbus.com'),
#         ('accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'),
#         ('accept-language', 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7'),
#         ('cache-control', 'max-age=0'),
#         # ('cookie', 'PHPSESSID=771k7892n521mh0o3ncebeohj6; existmag=mag; 4fJN_2132_seccodecSlqvwSe=27300.4c48839aa773245d55; age=verified; dv=1'),
#         ('cookie', '4fJN_2132_seccodecSeRRfg5=14339.4cce2e4f1ae59e531e; 4fJN_2132_seccodecSTVfEvf=9372.f1ae0a808eec67ca6a; 4fJN_2132_seccodecSXYwYAC=20246.0620c823cb43b800c7; 4fJN_2132_seccodecSM7ir7C=32974.501fed7ed7e50412ed; 4fJN_2132_seccodecSQTZPiM=26549.061809068ea08ce4ce; PHPSESSID=9ku0thftv26h49i683n1ml0ag1; existmag=mag; dv=1'),
#         ('Referer',Referer_url),
#         ('sec-ch-ua', 'sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="104", "Opera";v="90"'),
#         ('sec-ch-ua-mobile', '?0'),
#         ('sec-ch-ua-platform', '"Linux"'),
#         ('sec-fetch-dest', 'document'),
#         ('sec-fetch-mode', 'navigate'),
#         ('sec-fetch-site', 'same-origin'),
#         ('sec-fetch-user', '?1'),
#         ('upgrade-insecure-requests', '1'),
#         ('User-Agent',
#          'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84'),
#         ('X-Requested-With','XMLHttpRequest')
#     ]
#     urllib.request.install_opener(opener)

#     # Check if is supported bytes ranges
#     try:
#         with urllib.request.urlopen(url) as response:
#             if response.headers.get('Accept-Ranges') == 'bytes':
#                 bytes_ranges_supported = True
#     except:
#         pass


#     i = max_retries
#     while (i > 0):
#         i -= 1
#         try:
#             if bytes_ranges_supported:
#                 url.add_header('Range', 'bytes=%d-' % len(html_raw))
#                 with urllib.request.urlopen(url) as response:
#                     html_raw += response.read()
#                     break  # If the read was successful, break the loop
#             else:
#                 with urllib.request.urlopen(url) as response:
#                     html_raw = response.read()
#                     break  # If the read was successful, break the loop
#         except IncompleteRead as err:
#             html_raw += err.partial
#             if not bytes_ranges_supported and (unsafe or i == 0):
#                 break  # If bytes ranges not supported and unsafe or no retries left, break the loop
#         except:
#             raise
        
#         finally:
#             try:
#                 time.sleep(0.010)
#             except OSError:
#                 break
#             except KeyboardInterrupt:
#                 raise
    
#     soup = BeautifulSoup(html_raw.decode('utf-8', errors='ignore'), 'html.parser')
#     html = soup.prettify()
#     return html

# def get_html(url, Referer_url=None, max_retries=5):
#     '''get_html(url),download and return html'''
#     # if Referer_url:
#     #     headers['Referer'] = Referer_url
#     # req = requests.get(url, headers=headers)
#     # return req.content

#     if Referer_url==None:
#         Referer_url = url

#     if max_retries<1:
#         max_retries = 1

#     proxy = urllib.request.ProxyHandler({'https': proxy_addr})
#     opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
#     opener.addheaders = [
#         ('authority', 'www.javbus.com'),
#         ('accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'),
#         ('accept-language', 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7'),
#         ('cache-control', 'max-age=0'),
#         # ('cookie', 'PHPSESSID=771k7892n521mh0o3ncebeohj6; existmag=mag; 4fJN_2132_seccodecSlqvwSe=27300.4c48839aa773245d55; age=verified; dv=1'),
#         ('cookie', '4fJN_2132_seccodecSeRRfg5=14339.4cce2e4f1ae59e531e; 4fJN_2132_seccodecSTVfEvf=9372.f1ae0a808eec67ca6a; 4fJN_2132_seccodecSXYwYAC=20246.0620c823cb43b800c7; 4fJN_2132_seccodecSM7ir7C=32974.501fed7ed7e50412ed; 4fJN_2132_seccodecSQTZPiM=26549.061809068ea08ce4ce; PHPSESSID=9ku0thftv26h49i683n1ml0ag1; existmag=mag; dv=1'),
#         ('Referer',Referer_url),
#         ('sec-ch-ua', 'sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="104", "Opera";v="90"'),
#         ('sec-ch-ua-mobile', '?0'),
#         ('sec-ch-ua-platform', '"Linux"'),
#         ('sec-fetch-dest', 'document'),
#         ('sec-fetch-mode', 'navigate'),
#         ('sec-fetch-site', 'same-origin'),
#         ('sec-fetch-user', '?1'),
#         ('upgrade-insecure-requests', '1'),
#         ('User-Agent',
#          'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84'),
#         ('X-Requested-With','XMLHttpRequest')
#     ]
#     urllib.request.install_opener(opener)

#     for i in range(max_retries):
#         try:
#             soup = BeautifulSoup(urllib.request.urlopen(url).read().decode('utf-8', errors='ignore'), 'html.parser')
#             break
#         # except Exception as ret:
#         #     raise Exception(ret)
#         #     # print(ret)
#         # except IncompleteRead:
#         except Exception as err:
#             print(err)
#             if i == (max_retries -1):
#                raise     # give up after max_retries attempts

#     html = soup.prettify()
#     return html

headers = {
    'authority': 'www.javbus.com',
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    'cookie': '4fJN_2132_seccodecSeRRfg5=14339.4cce2e4f1ae59e531e; 4fJN_2132_seccodecSTVfEvf=9372.f1ae0a808eec67ca6a; 4fJN_2132_seccodecSXYwYAC=20246.0620c823cb43b800c7; 4fJN_2132_seccodecSM7ir7C=32974.501fed7ed7e50412ed; 4fJN_2132_seccodecSQTZPiM=26549.061809068ea08ce4ce; PHPSESSID=9ku0thftv26h49i683n1ml0ag1; existmag=mag; dv=1',
    'referer': 'https://www.javbus.com',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="104", "Opera";v="90"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84',
    'X-Requested-With': 'XMLHttpRequest',
};

proxies = {
  "http": "http://127.0.0.1:8118",
  "https": "http://127.0.0.1:8118",
}

def get_html(url, Referer_url=None, max_retries=5):
    '''get_html(url),download and return html'''
    if Referer_url==None:
        Referer_url = url

    if Referer_url:
        headers['Referer'] = Referer_url

    if max_retries<1:
        max_retries = 1

    for i in range(max_retries):
        try:
            response = requests.get(url, headers=headers, proxies=proxies, timeout=10)
            if response.status_code == 200:
                break
            elif response.status_code == 404:
                response.raise_for_status() # raise an HTTPError exception at once, if 404 err happens

        except Exception as err:
            # print(err)
            if i == (max_retries -1):
               raise     # other exceptions raised after max_retries attempts

    html = response.content
    soup = BeautifulSoup(html.decode('utf-8', errors='ignore'), 'html.parser')
    html = soup.prettify()
    return html
