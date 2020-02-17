from .Channel import Channel


class ForwardOption:
    def __init__(self, from_channel: Channel, to_channel: Channel):
        self.from_channel = from_channel
        self.to_channel = to_channel
