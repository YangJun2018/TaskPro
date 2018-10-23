# coding:utf-8
__author__ = 'YangJun'

import time

nowtime = time.localtime(time.time())
t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(t)
