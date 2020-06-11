import csv
import datetime
from classes import Channel


class FileWorker:
    def __init__(self, filename: str):
        self.filename = filename
        self.__fetch_channels__()

    def __fetch_channels__(self):
        self.channels = []
        file = open(self.filename, mode='r')
        reader = csv.DictReader(file, delimiter=',')
        for line in reader:
            self.channels.append(
                Channel(line["identifier"], line["name"], datetime.datetime.today()))

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        return self
