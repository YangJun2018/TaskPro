# coding:utf-8
__author__ = 'YangJun'

import subprocess, time, os

while True:
    info = subprocess.getoutput("cat /proc/meminfo")
    print(info)
    # 分离出不同指标
    para = info.split("\n")
    # 获取系统内存信息
    MemTotal = int(para[0].strip().split()[1])
    MemFree = int(para[1].strip().split()[1])
    Buffers = int(para[3].strip().split()[1])
    Cached = int(para[4].strip().split()[1])
    avaMem = round(((MemFree + Buffers + Cached) / MemTotal), 2)
    # 转换成百分数
    # avaMem = str(avaMem * 100) + '%'
    # nowtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # cache = nowtime + "   " + avaMem
    memUsage = '%s     %.2f%%' % (time.strftime('%Y%m%d_%H:%M:%S'), avaMem)
    # 新建文件
    subprocess.call("touch ret.txt", shell=True)
    with open("ret.txt", "a") as f1:
        f1.write(memUsage + '\n')
        f1.close()
    time.sleep(5)
    continue
