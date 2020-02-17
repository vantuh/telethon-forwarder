from telethon import TelegramClient
import os
from classes import ForwardOption, Channel
from utils import ChannelListner, FileWorker
from services import PrinterService


class Forwarder:
    def __init__(self):
        with TelegramClient(os.environ['SESSION_NAME'], os.environ['API_ID'], os.environ['API_HASH']) as client:
            for (dirpath, dirnames, filenames) in os.walk(os.environ['CHANNELS_DIR']):
                for filename in filenames:
                    with FileWorker("%s/%s" % (dirpath, filename)) as file_worker:
                        for channel in file_worker.channels:
                            ChannelListner(client, ForwardOption(channel, Channel('%s' % (os.path.splitext(filename)[0]), '', 1)))

            client.run_until_disconnected()


forwarder = Forwarder()
