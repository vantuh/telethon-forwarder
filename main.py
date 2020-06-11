from telethon import TelegramClient
import os
from classes import ForwardOption, Channel
from utils import ChannelListner, FileWorker


class Forwarder:
    def __init__(self):
        with TelegramClient(os.getenv("SESSION_NAME"), os.getenv("API_ID"), os.getenv("API_HASH")) as client:
            for dirpath, _, filenames in os.walk(os.getenv("CHANNELS_DIR")):
                for filename in filenames:
                    if filename.endswith(".csv"):
                        with FileWorker("%s/%s" % (dirpath, filename)) as file_worker:
                            if len(file_worker.channels) > 1:
                                to_channel = Channel(
                                    file_worker.channels[0].identifier, file_worker.channels[0].name, 1)
                                ChannelListner(client, ForwardOption(
                                    file_worker.channels, to_channel))

            client.run_until_disconnected()


forwarder = Forwarder()
