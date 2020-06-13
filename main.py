from telethon import TelegramClient
import os

from utils import ChannelListner


class Forwarder:
    def __init__(self):
        with TelegramClient(os.getenv("SESSION_NAME"), os.getenv("API_ID"), os.getenv("API_HASH")) as client:
            for dirpath, _, filenames in os.walk(os.getenv("CHANNELS_DIR")):
                for filename in filenames:
                    if filename.endswith(".csv"):
                        ChannelListner(client, "%s/%s" % (dirpath, filename))

            client.run_until_disconnected()


forwarder = Forwarder()
