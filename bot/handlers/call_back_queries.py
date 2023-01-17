from handlers import admin_handlers
from config import bot, channel_id
from telebot import types
from utils import Utils


@bot.callback_query_handler(func=lambda query: query.data == 'is_joined')
def check_is_joined(call: types.CallbackQuery):
    if not Utils().is_in_channel(call.message.chat.id, bot):
        bot.answer_callback_query(
            call.id, "هنوز عضو کانال ها نشدید", show_alert=True)
    else:
        admin_handlers.start_handler(call.message)
        bot.delete_message(call.message.chat.id, call.message.id)


@bot.callback_query_handler(func=lambda query: query.data == 'dont_send_server')
def dont_send_serever(call: types.CallbackQuery):
    bot.delete_message(call.message.chat.id, call.message.id)


@bot.callback_query_handler(func=lambda query: query.data == 'send_server')
def send_serever(call: types.CallbackQuery):
    bot.send_message(channel_id,
                     call.message.text,
                     parse_mode='HTML',
                     disable_web_page_preview=True,
                     )
    bot.delete_message(call.message.chat.id, call.message.id)
