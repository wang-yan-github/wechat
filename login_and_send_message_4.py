from wxpy import Bot, embed
import requests

# 登录微信
bot = Bot()

def send_msg(userName):
    info = '感悟：' + get_text()
    bot.file_helper.send(info)
    user = bot.friends().search(userName)[0]
    user.send(info)

def get_text():
    url = 'https://v1.hitokoto.cn/?c=d&c=k&encode=text'
    response = requests.get(url)
    return response.text

@bot.register()
def get_user_name(msg):
    NickName = '测试感悟发送1'  # Change this to the actual nickname you are looking for
    chatrooms = bot.groups(update=True)
    for chatroom in chatrooms:
        print(f"chatroom: {chatroom}")
        if chatroom.nick_name == NickName:
            print(f"NickName: {chatroom.user_name}")
            return chatroom.user_name

if __name__ == '__main__':
    userName = get_user_name(None)
    if userName:
        send_msg(userName)
    else:
        print('没有找到指定的聊天群')
    print('程序结束')

    # 保持程序运行
    embed()
