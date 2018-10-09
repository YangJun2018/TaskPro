#coding:utf-8
__author__ = 'Administrator'

import re



def ip_check(ip):

    #ipv4校验
    match_4=re.compile(r"^(1\d{2}|2[0-4]\d|25[0-5]|\d|[1-9]\d).(1\d{2}|2[0-4]\d|25[0-5]|\d|[1-9]\d)."
                       r"(1\d{2}|2[0-4]\d|25[0-5]|\d|[1-9]\d).(1\d{2}|2[0-4]\d|25[0-5]|\d|[1-9]\d)$")
    #ipv6格式校验
    match_6=re.compile(r"():():():()")
    if ":" in ip:
        if match_6.match(ip):
            print("this is correct ipv6")
        else:
            print("this is wrong ipv6")
    else:
        if match_4.match(ip):
            print("this is correct ipv4")
        else:
            print("this is wrong ipv4")


if __name__=="__main__":
    ip_check(ip="10.01.12.65")
