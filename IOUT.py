import asyncio
from telethon import TelegramClient
import datetime
import pytz

utc = pytz.UTC


class PrinterService(TelegramClient):
    def __init__(self, client):
        self.client = client

    def print_today_history(self, name):
        asyncio.ensure_future(self.__print_today_history__(name))

    async def __print_today_history__(self, name):
        today = datetime.datetime(datetime.datetime.today().year,
                                  datetime.datetime.today().month,
                                  datetime.datetime.today().day)
        async for message in self.client.iter_messages(name):
            if message.date.replace(tzinfo=utc) > today.replace(tzinfo=utc):
                print(message.id)

    def print_dialogs(self):
        asyncio.ensure_future(self.__print_dialogs__())

    async def __print_dialogs__(self):
        dialogs = await self.client.get_dialogs()
        for dialog in dialogs:
            print(dialog.name, ':', dialog.message.to_id)
