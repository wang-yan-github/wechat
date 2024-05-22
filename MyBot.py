import asyncio, os
from typing import List, Optional, Union

from wechaty_puppet import FileBox  # type: ignore

from wechaty import Wechaty, Contact
from wechaty.user import Message, Room


class MyBot(Wechaty):

    async def on_message(self, msg: Message):
        """
        listen for message event
        """
        from_contact: Optional[Contact] = msg.talker()
        text = msg.text()
        room: Optional[Room] = msg.room()
        if text == 'ding':
            conversation: Union[
                Room, Contact] = from_contact if room is None else room
            await conversation.ready()
            await conversation.say('dong')
            file_box = FileBox.from_url(
                'https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/'
                'u=1116676390,2305043183&fm=26&gp=0.jpg',
                name='ding-dong.jpg')
            await conversation.say(file_box)

os.environ['TOKEN'] = "puppet_donut_e7ce4cf8a1ab789166c39c6"
asyncio.run(MyBot().start())
