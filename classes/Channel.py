import datetime


class Channel:
    def __init__(self, identifier, name: str, last_message_date: datetime = datetime.datetime.today()):
        self.identifier = identifier
        self.name = name
        self.last_message_date = last_message_date

    def __str__(self):
        template = '%s : %s : %s' % (
            self.name, self.identifier, self.last_message_date)
        return template
