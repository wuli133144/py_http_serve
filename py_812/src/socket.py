
#!_*_coding:utf-8_*_
#__author__:'jackwu'

from socket 
import queue
import sys

print ("9>>>>>>")
s = socket.socket()         # 创建 socket 对象
print("11>>>>>>>>")
host =gethostname() # 获取本地主机名
port = 12345                # 设置端口
s.bind((host, port))        # 绑定端口

s.listen(5)                 # 等待客户端连接
while True:
    c, addr = s.accept()     # 建立客户端连接。
    c.send('欢迎访问菜鸟教程！')
    c.close()                # 关闭连接