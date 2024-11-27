#!/usr/bin/env python
#-*-coding:utf-8-*-

import sys
import controler
import downloader
import pageparser
import time
from requests.exceptions import HTTPError

def get_dict(url):
    """get the dict of the detail page and yield the dict"""

    url_html = downloader.get_html(url)
    for detail_url in pageparser.parser_homeurl(url_html):
        try:
            detail_page_html = downloader.get_html(detail_url)
            dict_jav = pageparser.parser_content(detail_page_html)
        # except Exception as err:
        #     with open('fail_url.txt', 'a') as fd:
        #         fd.write('%s %d: %s\n' % ('ERROR CODE', err.code, url))
        #     print("Fail to crawl %s\ncrawl next detail page......" % detail_url)
        #     continue
        except HTTPError as err:
            if err.response.status_code == 404:
                with open('404_url.txt', 'a') as fd:
                    fd.write('%s\n' % detail_url)
            else:
                with open('fail_url.txt', 'a') as fd:
                    fd.write('%s\n' % detail_url)
            print("Fail to crawl %s\ncrawl next detail page......" % detail_url)
            continue
        except Exception as err:
            with open('fail_url.txt', 'a') as fd:
                fd.write('%s\n' % detail_url)
            print("Fail to crawl %s\ncrawl next detail page......" % detail_url)
            continue

        yield dict_jav, detail_url


def get_data_single(url):
    """get the dict of the detail page and yield the dict"""

    try:
        detail_page_html = downloader.get_html(url)
        dict_jav = pageparser.parser_content(detail_page_html)
    except HTTPError as err:
        if err.response.status_code == 404:
            with open('404_url.txt', 'a') as fd:
                fd.write('%s\n' % url)
        else:
            with open('fail_url.txt', 'a') as fd:
                fd.write('%s\n' % url)
        print("Fail to crawl %s\ncrawl next detail page......" % url)
    except Exception as err:
        with open('fail_url.txt', 'a') as fd:
            fd.write('%s\n' % url)
        print("Fail to crawl %s\ncrawl next detail page......" % url)
    else:
        yield dict_jav

def join_db(url,is_uncensored):
    """the detail_dict of the url join the db"""

    for dict_jav_data, detail_url in get_dict(url):
        if controler.check_url_not_in_table(detail_url):
            print("detail_url = %s not exist" % detail_url)
            controler.write_data(dict_jav_data, is_uncensored)
        else:
            print("detail_url = %s exists" % detail_url)
            continue
            # print("it has updated over...window will be closed after 60s")
            # time.sleep(60)
            # exit()

def join_db_single(url,is_uncensored):
    """the detail_dict of the url join the db"""

    for dict_jav_data in get_data_single(url):
        if dict_jav_data == None:
            return

        if controler.check_url_not_in_table(url):
            print("detail_url = %s not exist" % url)
            controler.write_data(dict_jav_data, is_uncensored)
        else:
            print("detail_url = %s exists" % url)
            continue

def homeurl_handler(entrance):
    if entrance[-1] =='/':
        entrance = entrance[:-1]
    #创建数据表
    controler.create_db()
    #无码为1，有码为0
    is_uncensored = 1 if 'uncensored' in entrance else 0
    join_db(entrance, is_uncensored)

    entrance_html = downloader.get_html(entrance)
    next_page_url = pageparser.get_next_page_url(entrance, entrance_html)
    while True:
        if next_page_url != None:
            join_db(next_page_url,is_uncensored)
        else:
            break
        next_page_html = downloader.get_html(next_page_url)
        next_page_url = pageparser.get_next_page_url(entrance, next_page_html)

def singleurl_handler(entrance):
    if entrance[-1] =='/':
        entrance = entrance[:-1]
    #创建数据表
    controler.create_db()
    #无码为1，有码为0
    is_uncensored = 1 if 'uncensored' in entrance else 0
    join_db_single(entrance, is_uncensored)

if __name__ == '__main__':
    homeurl_handler('https://www.javbus.com/ja')
    homeurl_handler('https://www.javbus.com/ja/uncensored')
    # homeurl_handler('https://www.javbus.com/ja/SDJS-271') # 1 + 5
    # singleurl_handler('https://www.javbus.com/ja/SDJS-271')
    # singleurl_handler('https://www.javbus.com/ja/SP-1000') # test 404 error
    # singleurl_handler('https://www.javbus.com/ja/page/6') # test err url
    # singleurl_handler('https://www.javbus.com/ja/HEYZO-3379') # test uncensored
    # singleurl_handler('https://www.javbus.com/ja/EZD-269') # test bad page
    # homeurl_handler(sys.argv[1])
    #singleurl_handler(sys.argv[1])

