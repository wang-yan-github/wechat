import asyncio
from wechaty import Wechaty, Contact
import schedule
import time

class MyBot(Wechaty):
    async def on_ready(self):
        print('Bot is ready')
        # 初始化任务调度
        self.init_schedule()

    async def send_message(self):
        contact = await self.Contact.find('许剑')  # 替换为好友的微信昵称
        if contact:
            await contact.say('Hello, this is an automated message sent by a schedule task!')
        else:
            print('Friend not found')

    def init_schedule(self):
        # 定时任务，每天的特定时间发送消息
        schedule.every().day.at("14:30").do(asyncio.run_coroutine_threadsafe, self.send_message(), asyncio.get_event_loop())
        # 开启任务调度循环
        while True:
            schedule.run_pending()
            time.sleep(1)

    async def on_message(self, msg):
        from_contact = msg.talker()
        text = msg.text()
        print(f'Message from {from_contact.name}: {text}')

bot = MyBot()
asyncio.run(bot.start())
