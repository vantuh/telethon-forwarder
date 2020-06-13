from telethon import events
from classes import Channel
from utils import FileWorker
import os


class LoggerService(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(LoggerService, cls).__new__(cls)
        return cls.instance

    def log_event(self, event):
        print('%s' % (event))

    def log_channel(self, channel: Channel):
        print('[%s] mapped...' % (channel.name))
