# -*- coding: utf-8 -*-
import csv
import time
from wxpy import *

def read_info():
    f = open('./sample.csv','r',encoding="utf8")
    reader = csv.DictReader(f)
    return [info for info in reader]

def make_msg(raw_info):
    t = '这条消息由python自动发送。{n}-同学请于{t}时间参加{s}课程，课程地址是{a}。收到请回复，谢谢!'
    return [t.format(n = info['姓名'],
                     t = info['上课时间'],
                     s = info['课程'],
                     a = info['上课地址']
                     ) for info in raw_info]

def send(msg_list):
    bot = Bot()
    for msg in msg_list:
        fren_name = msg.split('-')[0]
        f = bot.friends().search(fren_name)
        if len(f) == 1:
            f[0].send(msg)
        else:
            print(fren_name)
            print('please check this name')
    time.sleep(3)

raw_info = read_info()
msg_list = make_msg(raw_info)
send(msg_list)