import itchat
import requests

itchat.auto_login()

def send_msg(friend_name):
    itchat.send('Hello, filehelper', toUserName='filehelper')

    author = itchat.search_friends(nickName=friend_name)[0]
    info = '感悟：' + get_text()
    author.send(info)

def get_text():
    url = 'https://v1.hitokoto.cn/?c=d&c=k&encode=text'
    response = requests.get(url)
    # print(response.text)
    return response.text

if __name__ == '__main__':
    friend_name = "君临"
    send_msg(friend_name)
    # get_text()
    print('程序结束')