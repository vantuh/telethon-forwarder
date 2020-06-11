FROM python:3

ADD . /app
WORKDIR /app

RUN pip3 install pytz
RUN pip3 install python-dotenv
RUN pip3 install telethon

CMD [ "python3", "./main.py" ]
