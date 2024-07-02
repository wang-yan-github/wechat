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
        itchat.auto_login(hotReload=True, enableCmdQR=2)  # 使用命令行显示二维码
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
            print(f"Fetching from URL: {url}")  # 打印 URL，以便确认
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
            if weekday in [0, 1, 2, 3]:
                userName = get_user_name('DNF-TouchFish')
                if userName:
                    send_msg(userName)
                    print('消息已发送')
        except Exception as e:
            print(f"Job failed: {e}")

    # 首次启动时立即执行一次
    auto_login_and_send_msg()

    # 设置定时任务，每天的 14:40 执行一次
    schedule.every().day.at("20:10").do(auto_login_and_send_msg)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    auto_login_and_send_msg()
