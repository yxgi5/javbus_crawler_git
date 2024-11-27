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

def join_db(url):
    """the detail_dict of the url join the db"""
    bango_in_page_cnt = 0
    for dict_jav_data, detail_url in get_dict(url):
        if controler.check_url_not_in_table(detail_url):
            print("detail_url = %s not exist" % detail_url)
            controler.write_data(dict_jav_data)
        else:
            if dict_jav_data['磁力链接'] == controler.read_magnets_from_table(detail_url)[0][0]:
                print("detail_url = %s exists" % detail_url)
                bango_in_page_cnt = bango_in_page_cnt + 1
                continue
                # print("it has updated over...window will be closed after 60s")
                # time.sleep(60)
                # exit()
            else:
                print("detail_url = %s updating" % detail_url)
                controler.refresh_data(dict_jav_data, detail_url)
    return bango_in_page_cnt

def join_db_single(url):
    """the detail_dict of the url join the db"""

    for dict_jav_data in get_data_single(url):
        if dict_jav_data == None:
            return

        if controler.check_url_not_in_table(url):
            print("detail_url = %s not exist" % url)
            controler.write_data(dict_jav_data)
        else:
            if dict_jav_data['磁力链接'] == controler.read_magnets_from_table(url)[0][0]:
                print("detail_url = %s exists" % url)
                continue
            else:
                print("detail_url = %s updating" % url)
                controler.refresh_data(dict_jav_data, url)

def homeurl_handler(entrance):
    if entrance[-1] =='/':
        entrance = entrance[:-1]
    #创建数据表
    controler.create_db()

    if join_db(entrance) == 30:
        return

    entrance_html = downloader.get_html(entrance)
    next_page_url = pageparser.get_next_page_url(entrance, entrance_html)
    while True:
        if next_page_url != None:
            if join_db(next_page_url) == 30:
                break
        else:
            break
        next_page_html = downloader.get_html(next_page_url)
        next_page_url = pageparser.get_next_page_url(entrance, next_page_html)

def singleurl_handler(entrance):
    if entrance[-1] =='/':
        entrance = entrance[:-1]
    #创建数据表
    controler.create_db()

    join_db_single(entrance)

if __name__ == '__main__':
    homeurl_handler('https://www.javbus.com/ja')
    homeurl_handler('https://www.javbus.com/ja/uncensored')
    # homeurl_handler('https://www.javbus.com/ja/SDJS-271') # 1 + 5
    # singleurl_handler('https://www.javbus.com/ja/SDJS-271')
    # singleurl_handler('https://www.javbus.com/ja/SP-1000') # test 404 error
    # singleurl_handler('https://www.javbus.com/ja/page/6') # test err url
    # singleurl_handler('https://www.javbus.com/ja/HEYZO-3379') # test uncensored
    # singleurl_handler('https://www.javbus.com/ja/EZD-269') # test bad page
    # singleurl_handler('https://www.javbus.com/ja/SDDL-478')
    # singleurl_handler('https://www.javbus.com/ja/BIG-054')
    # singleurl_handler('https://www.javbus.com/ja/FAA-250')
    # singleurl_handler('https://www.javbus.com/ja/STCV-036')
    # homeurl_handler(sys.argv[1])
    # singleurl_handler(sys.argv[1])
	# singleurl_handler('https://www.javbus.com/ja/' + sys.argv[1])

