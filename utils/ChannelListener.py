from telethon import TelegramClient, events
from classes import ForwardOption, Channel


class ChannelListner:
    def __init__(self, client: TelegramClient, option: ForwardOption):
        self.client = client
        self.option = option

        self.numeric_channels_identifiers = []
        self.text_channels_identifiers = []
        print('--- [%s] ---' % (option.to_channel.name))
        for channel in option.from_channels[1:]:
            print('[%s] mapped...' % (channel.name))
            if channel.identifier.isdigit():
                self.numeric_channels_identifiers.append(int(channel.identifier))
            else:
                self.text_channels_identifiers.append(channel.identifier)

        self.__chats_listener__()
        self.__ids_listener__()

    def __chats_listener__(self):
        if len(self.text_channels_identifiers) > 0:
            @self.client.on(events.NewMessage(chats=self.text_channels_identifiers))
            async def normal_handler(event):
                await self.client.forward_messages(self.option.to_channel.identifier, event.message)

    def __ids_listener__(self):
        if len(self.numeric_channels_identifiers) > 0:
            @self.client.on(events.NewMessage)
            async def normal_handler(event):
                for channel in self.numeric_channels_identifiers:
                    if event.message.to_id.channel_id == channel:
                        await self.client.forward_messages(self.option.to_channel.identifier, event.message)

    def __log_message__(self, message):
        print('[MSG] %s reposted to [%s]...' % (message.id, self.option.to_channel.identifier))
