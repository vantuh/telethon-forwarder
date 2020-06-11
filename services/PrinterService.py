import asyncio
from telethon import TelegramClient, helpers
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
        loop = asyncio.get_event_loop()
        try:
            loop.run_until_complete(self.__print_dialogs__())
        except asyncio.CancelledError as expression:
            print('Dialogs can\'t be printed.\n%s', expression)
        finally:
            loop.close()
            asyncio.set_event_loop(asyncio.new_event_loop())

    async def __print_dialogs__(self):
        dialogs = helpers.TotalList(await self.client.get_dialogs())
        for dialog in dialogs:
            print(dialog)
