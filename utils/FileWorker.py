import pandas as pd
import datetime
from classes import Channel


class FileWorker:
    def __init__(self, filename: str):
        self.filename = filename
        self.dataframe = pd.read_csv(self.filename, delimiter=',')

    def fetch_channels(self) -> [Channel]:
        channels = []
        for row in self.dataframe.itertuples():
            channels.append(
                Channel(row.identifier, row.name, row.date))
        return channels

    def append_date(self, identifier, date):
        self.dataframe.loc[self.dataframe.identifier ==
                           str(identifier), 'date'] = date
        self.dataframe.to_csv(self.filename)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        return self
