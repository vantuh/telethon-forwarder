from .Channel import Channel


class ForwardOption:
    def __init__(self, from_channels: list, to_channel: Channel):
        self.from_channels = from_channels
        self.to_channel = to_channel
