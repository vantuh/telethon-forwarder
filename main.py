from telethon import TelegramClient
import utils
from classes import ForwardOption
from utils import Listner


class Forwarder(list):
    def __init__(self, options):
        self.client = TelegramClient(utils.VARIABLES.SESSION['NAME'],
                                     utils.VARIABLES.SESSION['API_ID'],
                                     utils.VARIABLES.SESSION['API_HASH'])
        for option in options:
            Listner(self.client, option)
        self.client.start()
        self.client.run_until_disconnected()


forward_options = []
# forward_options.append(ForwardOption('MemeList',
#                                      utils.VARIABLES.CHANNELS['MEME_CHANNELS'],
#                                      utils.VARIABLES.CHANNELS['HOST_CHANNEL']))
forward_options.append(ForwardOption('ClosedList',
                                     utils.VARIABLES.CHANNELS['CLOSED_CHANNELS'],
                                     utils.VARIABLES.CHANNELS['HOST_CHANNEL']))

forwarder = Forwarder(forward_options)
