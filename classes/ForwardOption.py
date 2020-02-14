from classes.Channel import Channel


class ForwardOption:
    def __init__(self, name: str, channels: list, forward_channel: Channel):
        self.name = name
        self.channels_list = channels
        self.forward_channel = forward_channel
