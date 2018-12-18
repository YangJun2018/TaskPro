# coding:utf-8
__author__ = 'YangJun'
import pyperclip, random, string, socket, struct

print(chr(65))
print(chr(random.randint(0x4e00, 0x9fa5)))
ipv4 = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
a = hex(random.randint(1, 0xffff)).replace('0x', '')
print(a)
# print(bin(a))
# print(struct.pack('>I', random.randint(1, 0xffffffff)))
