from telethon import TelegramClient, events
from classes import ForwardOption, Channel


class ChannelListner:
    def __init__(self, client: TelegramClient, option: ForwardOption):
        self.client = client
        self.option = option

        if option.from_channel.identifier.isdigit():
            self.__ids_listener__()
        else:
            self.__chats_listener__()

    def __chats_listener__(self):
        print(self.option.from_channel.identifier, self.option.to_channel.identifier)
        @self.client.on(events.NewMessage(chats=self.option.from_channel.identifier))
        async def normal_handler(event: events.NewMessage.Event):
            id = int(self.option.to_channel.identifier) if self.option.to_channel.identifier.isdigit() else self.option.to_channel.identifier
            await self.client.forward_messages(id, event.message)

    def __ids_listener__(self):
        @self.client.on(events.NewMessage)
        async def normal_handler(event: events.NewMessage.Event):
            if message.to_id.channel_id == self.option.from_channel.identifier:
                id = int(self.option.to_channel.identifier) if self.option.to_channel.identifier.isdigit() else self.option.to_channel.identifier
                await self.client.forward_messages(id, event.message)

    def __log__listener__(self):
        print('[Listener] for [%s] started...' % self.option.from_channel.name)

    def __log_message__(self, message):
        print('[MSG] %s from [%s] reposted to [%s]...' % (message.id, self.option.from_channel.name, self.option.to_channel.identifier))
