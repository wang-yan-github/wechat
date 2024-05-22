import pyautogui
import pyperclip
import time
import requests
def send_msg(friend):
    pyautogui.hotkey('ctrl', 'alt', 'w')    # Ctrl + alt + w 打开微信
    pyautogui.hotkey('ctrl', 'f')           # 搜索好友
    pyperclip.copy(friend)                  # 复制好友昵称到粘贴板
    pyautogui.hotkey('ctrl', 'v')           # 模拟键盘 ctrl + v 粘贴
    time.sleep(5)
    pyautogui.press('enter')                # 回车进入好友消息界面
    info = '感悟：' + get_text()
    pyperclip.copy(info)      
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press('enter')

def get_text():
    url = 'https://v1.hitokoto.cn/?c=d&c=k&encode=text'
    response = requests.get(url)
    # print(response.text)
    return response.text

if __name__ == '__main__':
    # friend_name = "鼎驰科技"		#对方用户名称：与微信备注保持一致，尽量使用英文
    friend_name = "我咯国宾"		#对方用户名称：与微信备注保持一致，尽量使用英文
    send_msg(friend_name)
    # get_text()
    print('程序结束')