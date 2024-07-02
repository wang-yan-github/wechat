import re
import sys
import json
import itchat
from itchat.content import *
import requests
import schedule
import time

def on_login():
    print("Login callback: success.")

def on_exit():
    print("Exit callback: success.")

def auto_login_and_send_msg():
    try:
        itchat.auto_login(hotReload=False, enableCmdQR=2)  # 每次启动要求重新扫描二维码
    except Exception as e:
        print(f"Login failed: {e}")
        return

    def send_msg(userName):
        try:
            info = '感悟：' + get_text()
            itchat.send(info, toUserName='filehelper')
            itchat.send(info, toUserName=userName)
        except Exception as e:
            print(f"Failed to send message: {e}")

    def get_text():
        try:
            url = 'https://v1.hitokoto.cn/?c=d&c=k&encode=text'
            response = requests.get(url)
            return response.text
        except Exception as e:
            print(f"Failed to get text: {e}")
            return ""

    def get_user_name(NickName):
        try:
            ins = itchat.instanceList[0]
            fullContact = ins.memberList + ins.chatroomList
            for chatroom in fullContact:
                if chatroom['NickName'] == NickName:
                    return chatroom.UserName
        except Exception as e:
            print(f"Failed to get user name: {e}")
            return ""

    def job():
        try:
            weekday = time.localtime().tm_wday
            if weekday in [0, 2, 4, 3]:
                userName = get_user_name('测试感悟发送1')
                if userName:
                    send_msg(userName)
                    print('消息已发送')
        except Exception as e:
            print(f"Job failed: {e}")

    job()

    # 首次启动时立即执行一次
    auto_login_and_send_msg()

if __name__ == '__main__':
    auto_login_and_send_msg()
    schedule.every().day.at("20:00").do(auto_login_and_send_msg)

    while True:
        schedule.run_pending()
        time.sleep(1)
