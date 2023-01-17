from apscheduler.schedulers.background import BackgroundScheduler
from requests.exceptions import ConnectionError, ReadTimeout
from handlers.bot import admin_handlers, user_handlers
from database.config import Base, engine
from handlers import call_back_queries
from config import bot, channel_id
from templates import Template
from random import choice
from telebot import types
from utils import Utils
import requests
import sys
import os


sched = BackgroundScheduler()
template = Template()

Base.metadata.create_all(engine)


bot.set_my_commands([
    types.BotCommand('/start', 'main menu'),
])


@bot.message_handler()
def not_valid_handler(message: types.Message):
    if Utils().is_admin(message.chat.id):
        bot.reply_to(message, 'That\'s not a valid command, try again.')
        return
    bot.reply_to(message, 'لطفا یک دستور معتبر وارد کنید.')


def send_proxy():
    raw_proxy = choice(requests.get(
        'https://mtpro.xyz/api/?type=mtproto').json())
    proxy = f'https://t.me/proxy?server={raw_proxy["host"]}&port={raw_proxy["port"]}&secret={raw_proxy["secret"]}'
    connect_menu = types.InlineKeyboardMarkup()
    connect_menu.add(types.InlineKeyboardButton(
        f"🟢 Connect with ping {raw_proxy['ping']} 🟢", callback_data=('connect'), url=proxy))
    bot.send_message(
        channel_id,
        template.create_proxy_template('Proxy', location=f'🌍 {raw_proxy["country"]}'), reply_markup=connect_menu
    )


sched.add_job(send_proxy, 'interval', hours=2)
sched.start()

if __name__ == '__main__':
    bot.delete_webhook()
    try:
        print('Bot Started Successfuly...')
        bot.infinity_polling(timeout=10, long_polling_timeout=5)
    except (ConnectionError, ReadTimeout) as e:
        sys.stdout.flush()
        os.execv(sys.argv[0], sys.argv)
    else:
        print('Bot Started Successfuly...')
        bot.infinity_polling(timeout=10, long_polling_timeout=5)
