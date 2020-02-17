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
                        id_str = os.path.splitext(filename)[0]
                        to_channel = Channel(id_str, id_str, 1)
                        ChannelListner(client, ForwardOption(file_worker.channels, to_channel))

            client.run_until_disconnected()


forwarder = Forwarder()
