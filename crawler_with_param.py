#!/usr/bin/env python
#-*-coding:utf-8-*-

import sys
import crawler
import time

if __name__ == '__main__':
	crawler.singleurl_handler('https://www.javbus.com/ja/' + sys.argv[1])

