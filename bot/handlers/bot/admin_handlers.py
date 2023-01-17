from handlers import admin_handlers, user_handlers
from telebot import types
from database import db
from config import bot
from utils import Utils


join_menu = types.InlineKeyboardMarkup()
join_button = types.InlineKeyboardButton(
    "FarasDv Vpn", callback_data='faras', url='https://t.me/FarasDvVpn')
confirm_btn = types.InlineKeyboardButton(
    "✅تایید عضویت ✅", callback_data='is_joined')
join_menu.add(join_button)
join_menu.add(confirm_btn)


def is_invite(text: str):
    return text.split()[1] if len(text.split()) > 1 else None


@bot.message_handler(regexp='start', func=lambda msg: is_invite(msg.text) is not None)
def invite_handler(message: types.Message):
    inviter_id = message.text.split()[1]
    if db.get_user(message.chat.id):
        if not Utils().is_in_channel(message.chat.id, bot):
            bot.send_message(message.chat.id,
                             'لطفا برای استفاده از ربات اول عضو کانال زیر شوید.', reply_markup=join_menu)
            return
        admin_handlers.start_handler(message, Utils().is_admin(message.chat.id))
        return
    user_handlers.invite_handler(message, inviter_id)
    if not Utils().is_in_channel(message.chat.id, bot):
        bot.send_message(message.chat.id,
                         'لطفا برای استفاده از ربات اول عضو کانال زیر شوید.', reply_markup=join_menu)
        return
    admin_handlers.start_handler(message, Utils().is_admin(message.chat.id))


@bot.message_handler(func=lambda msg: not Utils().is_in_channel(msg.chat.id, bot))
def check_is_in_channel(message: types.Message):
    bot.send_message(message.chat.id,
                     'لطفا برای استفاده از ربات اول عضو کانال زیر شوید.', reply_markup=join_menu)


@bot.message_handler(commands=['start'])
def start_handler(message: types.Message):
    admin_handlers.start_handler(message, Utils().is_admin(message.chat.id))


@bot.message_handler(regexp='🏠')
def start_handler(message: types.Message):
    admin_handlers.start_handler(message, Utils().is_admin(message.chat.id))


@bot.message_handler(regexp='➕ Post a new server ➕')
def enter_send_server_handler(message: types.Message):
    admin_handlers.enter_server_handler(message)
    bot.register_next_step_handler(message, post_server_handler)


def post_server_handler(message: types.Message):
    admin_handlers.post_server_handler(message)


@bot.message_handler(regexp='❗ Post a new infrom ❗')
def enter_regular_inform(message: types.Message):
    admin_handlers.enter_regular_inform(message)
    bot.register_next_step_handler(message, post_regular_inform)


def post_regular_inform(message: types.Message):
    admin_handlers.post_regular_inform(message)


@bot.message_handler(regexp='✉️ Message members ✉️')
def enter_message_members_handler(message: types.Message):
    admin_handlers.enter_message_members_handler(message)
    bot.register_next_step_handler(message, post_message_members_handler)


def post_message_members_handler(message: types.Message):
    admin_handlers.post_message_members_handler(message)


@bot.message_handler(regexp='📋 List members 📋')
def list_members_handler(message: types.Message):
    admin_handlers.list_members_handler(message)


@bot.message_handler(regexp='✏️ Edit Sponsers ✏️')
def edit_sponsers_handler(message: types.Message):
    admin_handlers.edit_sponsers_handler(message)


@bot.message_handler(regexp='✏️ Edit Sponsers ✏️')
def edit_sponsers_handler(message: types.Message):
    admin_handlers.edit_sponsers_handler(message)


@bot.message_handler(regexp='➕ Add a sponser ➕')
def add_sponser_handler(message: types.Message):
    admin_handlers.add_sponser_handler(message)
    bot.register_next_step_handler(message, post_sponser_handler)


def post_sponser_handler(message: types.Message):
    admin_handlers.enter_add_sponser_handler(message)


@bot.message_handler(regexp='❌ Remove a sponser ❌')
def remove_sponser_handler(message: types.Message):
    admin_handlers.remove_sponser_handler(message)
    bot.register_next_step_handler(message, enter_remove_sponser_handler)


def enter_remove_sponser_handler(message: types.Message):
    admin_handlers.enter_remove_sponser_handler(message)


@bot.message_handler(regexp='🧍🏻‍♂️ Go to user menu 🧍🏻‍♂️')
def enter_regular_inform(message: types.Message):
    admin_handlers.start_handler(message)


@bot.message_handler(regexp='🧍🏻‍♂️ Back to admin menu 🧍🏻‍♂️')
def enter_regular_inform(message: types.Message):
    admin_handlers.start_handler(message, Utils().is_admin(message.chat.id))
