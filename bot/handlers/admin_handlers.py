from keyboards.admin_keyboard import AdminKeyBoard
from keyboards.user_keyboard import UserKeyBoard
from config import bot, channel_id
from templates import Template
from telebot import types
from database import db
from utils import Utils


template = Template()
main_admin_menu = AdminKeyBoard().main_admin_menu
back_menu = AdminKeyBoard().back_menu


def post_server(message: types.Message):
    try:
        items = message.text.split('*')
        type = Utils().get_type_of_server(items[0].lower())
        server = items[1]
        if type == 'Proxy':
            connect_menu = types.InlineKeyboardMarkup()
            connect_menu.row_width = 2
            connect_menu.add(types.InlineKeyboardButton(
                "Connect", callback_data=('connect'), url=server))
            bot.send_message(
                channel_id,
                template.create_proxy_template(type), reply_markup=connect_menu
            )
        else:
            bot.send_message(
                channel_id,
                template.create_server_template(type, f'<code>{server}</code>'),  parse_mode='HTML'
            )
        bot.reply_to(message, 'Posted Successfuly ✅.')
        bot.send_message(
            message.chat.id, 'What else?', reply_markup=main_admin_menu)

    except Exception as e:
        if message.text == '🏠':
            bot.send_message(
                message.chat.id, 'Back to home.', reply_markup=main_admin_menu)
        else:
            bot.send_message(
                message.chat.id, 'That\'s not a valid url, try again.', reply_markup=main_admin_menu)


def start_handler(message: types.Message, is_admin: bool = False):
    user = message.chat
    db.post_user(user.id, user.first_name, user.username)
    if is_admin:
        bot.send_message(
            message.chat.id, f'Hey {message.chat.first_name}, What can i do for you?', reply_markup=main_admin_menu)
    else:
        main_user_menu = UserKeyBoard().main_user_menu
        if Utils().is_admin(message.chat.id):
            admin_menu_btn = types.KeyboardButton(
                '🧍🏻‍♂️ Back to admin menu 🧍🏻‍♂️')
            main_user_menu.add(admin_menu_btn)
        bot.send_message(
            message.chat.id, f'سلام {message.chat.first_name}، چه کاری از دستم بر میاد؟', reply_markup=main_user_menu)


def enter_server_handler(message: types.Message):
    bot.send_message(
        message.chat.id,
        'Please enter your server info like the above format:\n\n<code>server_type:server_address</code>',
        parse_mode='HTML',
        reply_markup=back_menu
    )


def post_server_handler(message: types.Message):
    if message.text.lower() == '🏠' or message.text.lower() == '/start':
        bot.send_message(message.chat.id, 'Back to home.',
                         reply_markup=main_admin_menu)
        return
    post_server(message)


def enter_regular_inform(message: types.Message):
    bot.send_message(message.chat.id, 'Enter your inform:',
                     reply_markup=back_menu)


def post_regular_inform(message: types.Message):
    if message.text.lower() == '🏠' or message.text.lower() == '/start':
        bot.send_message(message.chat.id, 'Back to home.',
                         reply_markup=main_admin_menu)
        return
    inform = template.create_inform_template(message.text)
    bot.send_message(channel_id, inform,  parse_mode='HTML'
                     )
    bot.reply_to(message, 'Posted Successfuly ✅.')
    bot.send_message(
        message.chat.id, 'What else?', reply_markup=main_admin_menu)


def enter_message_members_handler(message: types.Message):
    bot.send_message(message.chat.id, 'Enter your message:',
                     reply_markup=back_menu)


def post_message_members_handler(message: types.Message):
    if message.text.lower() == '🏠' or message.text.lower() == '/start':
        bot.send_message(message.chat.id, 'Back to home.',
                         reply_markup=main_admin_menu)
        return
    bot.send_message(message.chat.id, 'sending...')
    users = db.get_users()
    for user in users:
        bot.send_message(user.tel_id, message.text,
                         )

    bot.delete_message(message.chat.id, message.id+1)
    bot.reply_to(message, 'Messaged Successfuly ✅.')
    bot.send_message(
        message.chat.id, 'What else?', reply_markup=main_admin_menu)


def list_members_handler(message: types.Message):
    if message.text.lower() == '🏠' or message.text.lower() == '/start':
        bot.send_message(message.chat.id, 'Back to home.',
                         reply_markup=main_admin_menu)
        return
    bot.send_message(message.chat.id, 'wait...')
    users = db.get_users()
    listed_usres = 'Memebers:\n'
    for user in users:
        listed_usres += f'{user.first_name}: @{user.username}\n'

    bot.delete_message(message.chat.id, message.id+1)
    bot.reply_to(message, listed_usres)
    bot.send_message(
        message.chat.id, 'What else?', reply_markup=main_admin_menu)


def edit_sponsers_handler(message: types.Message):
    wait = bot.send_message(message.chat.id, 'wait...')
    edit_sponsers_menu = types.ReplyKeyboardMarkup()
    remove_sponser_btn = types.KeyboardButton('➕ Add a sponser ➕')
    add_sponser_btn = types.KeyboardButton('❌ Remove a sponser ❌')
    home_btn = types.KeyboardButton('🏠')
    edit_sponsers_menu.add(add_sponser_btn)
    edit_sponsers_menu.add(remove_sponser_btn)
    edit_sponsers_menu.add(home_btn)
    sponsers = db.get_sponsers()
    active_sponsers = 'Here\' the list of active sponsers:\n\n'
    for sponser in sponsers:
        active_sponsers += f'{sponser.id}.<a href="{sponser.channel_url}">{sponser.title}</a>\n'
    bot.delete_message(message.chat.id, wait.id)
    bot.send_message(
        message.chat.id, active_sponsers,
        reply_markup=edit_sponsers_menu,
        parse_mode='HTML',
        disable_web_page_preview=True
    )


def add_sponser_handler(message: types.Message):
    bot.send_message(
        message.chat.id,
        'Please enter the sponser info like the above format:\n\n<code>sponser_title:sponser_id</code>',
        parse_mode='HTML',
        reply_markup=types.ReplyKeyboardRemove()
    )


def enter_add_sponser_handler(message: types.Message):
    try:
        sponser_title = message.text.split(':')[0]
        sponser_url = message.text.split(':')[1]
        db.post_sponser(
            sponser_title, f'https://t.me/{sponser_url}')
        bot.reply_to(message, 'Added Successfuly ✅.')
        bot.send_message(
            message.chat.id, 'What else?', reply_markup=main_admin_menu)
    except Exception:
        bot.reply_to(message, 'That\'s not a valid format, try again.')
        bot.send_message(
            message.chat.id, 'What else?', reply_markup=main_admin_menu)


def remove_sponser_handler(message: types.Message):
    bot.send_message(
        message.chat.id,
        'Please enter the sponser id:',
        reply_markup=types.ReplyKeyboardRemove()
    )


def enter_remove_sponser_handler(message: types.Message):
    try:
        db.remove_sponser(int(message.text))
        bot.reply_to(message, 'Removed Successfuly ✅.')
        bot.send_message(
            message.chat.id, 'What else?', reply_markup=main_admin_menu)
    except Exception:
        bot.reply_to(message, 'There\'s no such a sponser.')
        bot.send_message(
            message.chat.id, 'What else?', reply_markup=main_admin_menu)
