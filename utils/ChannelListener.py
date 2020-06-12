from telethon import TelegramClient, events
from classes import ForwardOption, Channel
from .FileWorker import FileWorker


class ChannelListner:
    def __init__(self, client: TelegramClient, channels_filename: str):
        self.client = client
        self.file_worker = FileWorker(channels_filename)
        self.option = self.__construct_forward_option__()

        self.numeric_channels_identifiers = []
        self.text_channels_identifiers = []

        print('--- [%s] ---' % (self.option.to_channel.name))
        for channel in self.option.from_channels[1:]:
            print('[%s] mapped...' % (channel.name))
            if channel.identifier.isdigit():
                self.numeric_channels_identifiers.append(
                    int(channel.identifier))
            else:
                self.text_channels_identifiers.append(channel.identifier)

        self.__chats_listener__()
        self.__ids_listener__()

    def __construct_forward_option__(self):
        channels = self.file_worker.fetch_channels()
        if len(channels) > 1:
            return ForwardOption(channels, channels[0])

    def __chats_listener__(self):
        if len(self.text_channels_identifiers) > 0:
            @self.client.on(events.NewMessage(chats=self.text_channels_identifiers))
            async def normal_handler(event):
                # TODO: Unwrap event message object ot channel_id and modify date in .csv
                await self.client.forward_messages(self.option.to_channel.identifier, event.message)

    def __ids_listener__(self):
        if len(self.numeric_channels_identifiers) > 0:
            @self.client.on(events.NewMessage)
            async def normal_handler(event):
                for channel in self.numeric_channels_identifiers:
                    if event.message.to_id.channel_id == channel:
                        # TODO: Unwrap event message object ot channel_id and modify date in .csv
                        await self.client.forward_messages(self.option.to_channel.identifier, event.message)

    # TODO: Logger service
