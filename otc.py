import asyncio
import time

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from telethon import TelegramClient


print('Created by @soldier_of_art')

api_id, api_hash = '', ''  # https://my.telegram.org/apps
groups = []  # группа, в которую пишем сообщения, вот формат: [-6475849365, 'https://t.me/cake_otc_market']

client = TelegramClient('otc', api_id, api_hash)
scheduler = BackgroundScheduler()
scheduler.start()
client.start()

loop = asyncio.get_event_loop()


def send_messages():
    with open('message.txt', encoding='utf-8') as f:
        message_text = f.read()


    for group in groups:
        try:
            loop.run_until_complete(client.send_message(group, message_text))
            time.sleep(.09)
        except Exception as e:
            print(e)


scheduler.add_job(
    send_messages,
    trigger=IntervalTrigger(
        hours=int('1')
    )
)
send_messages()
input('Press Enter to exit!')