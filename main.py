from telethon import TelegramClient
import os
from classes import ForwardOption, Channel
from utils import ChannelListner, FileWorker


class Forwarder:
    def __init__(self):
        with TelegramClient(os.environ['SESSION_NAME'], os.environ['API_ID'], os.environ['API_HASH']) as client:
            for (dirpath, dirnames, filenames) in os.walk(os.environ['CHANNELS_DIR']):
                for filename in filenames:
                    with FileWorker("%s/%s" % (dirpath, filename)) as file_worker:
                        if len(file_worker.channels) > 1:
                            to_channel = Channel(file_worker.channels[0].identifier, file_worker.channels[0].name, 1)
                            ChannelListner(client, ForwardOption(file_worker.channels, to_channel))

            client.run_until_disconnected()


forwarder = Forwarder()
