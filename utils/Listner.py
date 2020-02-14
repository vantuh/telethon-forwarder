from telethon import TelegramClient, events
from classes import ForwardOption


class Listner:
    def __init__(self, client: TelegramClient, option: ForwardOption):
        self.client = client
        self.option = option

        if type(option.channels_list[0]) is int:
            self.__ids_listener__()
        elif type(option.channels_list[0]) is str:
            self.__chats_listener__()

    def __chats_listener__(self):
        print('[NAME-Listener]', self.option.name, 'started...')

        @self.client.on(events.NewMessage(chats=self.option.channels_list))
        async def normal_handler(event: events.NewMessage.Event):
            message = event.message
            await self.client.forward_messages(self.option.forward_channel, message)

    def __ids_listener__(self):
        print('[ID-Listener]', self.option.name, 'started...')

        @self.client.on(events.NewMessage)
        async def normal_handler(event):
            message = event.message
            for channel in self.option.channels_list:
                if message.to_id.channel_id == channel:
                    await client.forward_messages(self.option.forward_channel, message)
