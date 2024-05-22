import itchat
from apscheduler.schedulers.blocking import BlockingScheduler
import logging

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 定义一个全局变量来追踪登录状态
is_logged_in = False

def login_wechat():
    global is_logged_in
    try:
        # 登录微信
        logging.info('开始登录微信...')
        itchat.auto_login(hotReload=True)
        is_logged_in = True
        logging.info('登录成功')
    except Exception as e:
        is_logged_in = False
        logging.error(f'微信登录失败: {e}')

def send_message():
    try:
        # 获取群聊列表
        # chatrooms = itchat.get_chatrooms(update=True)
        chatrooms = itchat.search_chatrooms(name='TouchFish')

        logging.info(f'获取到的群聊列表: {chatrooms}')

        # 查找特定的群聊
        target_chatroom = None
        for chatroom in chatrooms:
            if '群聊名称' in chatroom['NickName']:  # 确保使用正确的字段
                target_chatroom = chatroom['UserName']
                break

        if target_chatroom:
            # 发送消息
            itchat.send('这是定时发送的消息', toUserName=target_chatroom)
            logging.info('消息发送成功')
        else:
            logging.warning("找不到指定的群聊")
    except Exception as e:
        logging.error(f'发送消息时发生错误: {e}')

def login_and_send_message():
    global is_logged_in
    try:
        if not is_logged_in:
            login_wechat()
        if is_logged_in:
            send_message()
    except Exception as e:
        logging.error(f'执行任务时发生错误: {e}')

# 初始化微信登录
login_wechat()

# 定时任务
scheduler = BlockingScheduler()
scheduler.add_job(login_and_send_message, 'interval', seconds=1)  # 每秒执行
logging.info('定时任务已启动')
try:
    scheduler.start()
except (KeyboardInterrupt, SystemExit):
    logging.info('定时任务已停止')
    itchat.logout()
