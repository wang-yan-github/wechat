import re
import sys
import json
import itchat
from itchat.content import *
import requests
import schedule
import time

def auto_login_and_send_msg():
    try:
        itchat.auto_login(hotReload=False, enableCmdQR=2)  # 每次启动要求重新扫描二维码
    except Exception as e:
        print(f"Login failed: {e}")
        return

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
        weekday = time.localtime().tm_wday
        if weekday in [0, 1, 2]:
            userName = get_user_name('测试感悟发送1')
            send_msg(userName)
            print('消息已发送')

    job()

if __name__ == '__main__':
    auto_login_and_send_msg()
    schedule.every().day.at("09:35").do(auto_login_and_send_msg)

    while True:
        schedule.run_pending()
        time.sleep(1)
