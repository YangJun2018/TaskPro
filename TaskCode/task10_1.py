# coding:utf-8
__author__ = 'YangJun'

import subprocess, time

info = subprocess.getoutput("cat /proc/meminfo")
print(info)
