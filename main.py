from telethon import TelegramClient, events
from channels import memeChannels, host_channel, closed_channels
from ENV import ENV


def main():
    print('Hello world')
    client = TelegramClient(ENV.SESSION_NAME, ENV.API_ID, ENV.API_HASH)
    # start_closed_channels_listener(client)
    start_meme_listener(client)
    client.start()
    client.run_until_disconnected()


def start_closed_channels_listener(client):
    print('[Listener] ClosedChannels started...')

    @client.on(events.NewMessage)
    async def normal_handler(event):
        for channel in closed_channels:
            if event.message.to_id.channel_id == channel:
                print(event.message)
                await client.forward_messages(host_channel, event.message)


def start_meme_listener(client):
    print('[Listener] MEMEs started...')

    @client.on(events.NewMessage(chats=memeChannels))
    async def normal_handler(event):
        await client.forward_messages(host_channel, event.message)


main()
