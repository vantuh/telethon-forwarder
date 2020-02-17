import csv
from classes import Channel
import datetime


class FileWorker:
    channels = []

    def __init__(self, file_name: str):
        self.file = open(file_name)
        self.__fetch_channels__()

    def __fetch_channels__(self):
        reader = csv.DictReader(self.file, delimiter=',')
        self.channels = []
        for line in reader:
            self.channels.append(Channel(line["identifier"], line["name"], datetime.datetime.today()))

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
