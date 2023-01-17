from handlers import user_handlers
from telebot import types
from config import bot



@bot.message_handler(regexp='🕊️ جدیدترین پروکسی ها 🕊️')
def newsest_proxies_handler(message: types.Message):
    user_handlers.newsest_proxies_handler(message)


@bot.message_handler(regexp='💯 ارسال سرور  💯')
def explain_send_server_handler(message: types.Message):
    user_handlers.explain_send_server_handler(message)
    bot.register_next_step_handler(message, enter_send_server_handler)


def enter_send_server_handler(message: types.Message):
    con = user_handlers.enter_send_server_handler(message)
    if con:
        bot.register_next_step_handler(message, post_send_server_handler)


def post_send_server_handler(message: types.Message):
    user_handlers.post_send_server_handler(message)


@bot.message_handler(regexp='🎰 دریافت سرور اختصاصی رایگان 🎰')
def reffral_handler(message: types.Message):
    user_handlers.reffral_handler(message)


@bot.message_handler(regexp='♻️ دریافت لینک عضوگیر ی من ♻️')
def my_link_handler(message: types.Message):
    user_handlers.my_link_handler(message)


@bot.message_handler(regexp='📊 آمار عضو گیری من 📊')
def my_points_handler(message: types.Message):
    user_handlers.my_points_handler(message)


@bot.message_handler(regexp='🎁 دریافت هدیه 🎁')
def my_gift_handler(message: types.Message):
    user_handlers.my_gift_handler(message)
    bot.register_next_step_handler(message, get_gift_handler)


def get_gift_handler(message: types.Message):
    user_handlers.get_gift_handler(message)


@bot.message_handler(regexp='💌 ارتباط با ما 💌')
def contact_us_handler(message: types.Message):
    user_handlers.contact_us_handler(message)
