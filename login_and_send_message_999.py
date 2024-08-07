import re
import sys
import json
import itchat
import itchat_uos
from itchat.content import *
import requests
import schedule
import time


def auto_login_and_send_msg():
    try:
        itchat_uos.auto_login(hotReload=True, enableCmdQR=2, loginMethod='pad')  # 每次启动要求重新扫描二维码
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
            print(f"chatroom: {chatroom}")
            if chatroom['NickName'] == NickName:
                print(f"chatroom.UserName: {chatroom.UserName}")
                return chatroom.UserName

    def job():
        weekday = time.localtime().tm_wday
        # 0：星期一
        # 1：星期二
        # 2：星期三
        # 3：星期四
        # 4：星期五
        # 5：星期六
        # 6：星期日
        if weekday in [0, 1, 2, 3]:
            userName = get_user_name('测试感悟发送1')
            send_msg(userName)
            userName = get_user_name('DNF-TouchFish')
            send_msg(userName)
            print('消息已发送')

    job()


if __name__ == '__main__':
    auto_login_and_send_msg()
    schedule.every().day.at("20:15").do(auto_login_and_send_msg)

    while True:
        schedule.run_pending()
        time.sleep(1)
