import re
import sys
import json
import itchat
from itchat.content import *
import requests
import schedule
import time

itchat.auto_login(enableCmdQR=True, hotReload=True)

def send_msg(userName):
    info = '感悟：' + get_text()
    itchat.send(info, toUserName='filehelper')
    itchat.send(info, toUserName=userName)


def get_text():
    url = 'https://v1.hitokoto.cn/?c=d&c=k&encode=text'
    response = requests.get(url)
    return response.text


def get_user_name(NickName):
    ins = itchat.instanceList[0]
    fullContact = ins.memberList + ins.chatroomList
    for chatroom in fullContact:
        if chatroom['NickName'] == NickName:
            return chatroom.UserName


def job():
    # 获取星期几
    weekday = time.localtime().tm_wday
    # 如果今天是星期一、星期二或星期三
    if weekday in [0, 1, 2]:
        userName = get_user_name('测试感悟发送1')
        send_msg(userName)
        print('消息已发送')


if __name__ == '__main__':
    # 每天定时检查
    schedule.every().day.at("19:40").do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)
