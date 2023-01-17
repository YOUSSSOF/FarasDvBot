from keyboards.user_keyboard import UserKeyBoard
from templates import Template
from telebot import types
from database import db
from config import bot
from utils import Utils
import requests

template = Template()


def what_else_home_handler(id, message):
    main_user_menu = UserKeyBoard().main_user_menu
    if Utils().is_admin(id):
        admin_menu_btn = types.KeyboardButton(
            '🧍🏻‍♂️ Back to admin menu 🧍🏻‍♂️')
        main_user_menu.add(admin_menu_btn)
    bot.send_message(
        id, message, reply_markup=main_user_menu)


def newsest_proxies_handler(message: types.Message):
    bot.send_message(
        message.chat.id,
        'در حال دریافت...'),

    connect_menu = types.InlineKeyboardMarkup(row_width=2)
    btns = []
    proxies = []
    raw_proxies = requests.get(
        'https://mtpro.xyz/api/?type=mtproto').json()[:6]
    for raw_proxy in raw_proxies:
        proxies.append(
            f'{raw_proxy["ping"]}!https://t.me/proxy?server={raw_proxy["host"]}&port={raw_proxy["port"]}&secret={raw_proxy["secret"]}')
    for proxy in proxies:
        ping = proxy.split('!')[0]
        url = proxy.split('!')[1]
        btns.append(types.InlineKeyboardButton(
            f"🟢 Connect with ping {ping} 🟢", callback_data=f'connect', url=url))
    for btn in btns:
        connect_menu.add(btn)

    bot.delete_message(message.chat.id, message.id+1)
    bot.send_message(
        message.chat.id,
        'پرسرعت ترین پروکسی ها 👇', reply_markup=connect_menu
    )
    what_else_home_handler(message.chat.id, 'دیگه چیکار میتونم برات بکنم؟')


def contact_us_handler(message: types.Message):
    bot.reply_to(message, 'لطفا برای انتقاد، پیشنهاد و مشاوره با آیدی زیر در  تماس باشید 🍷👇\n\n@FarasDvSupport '
                 )
    what_else_home_handler(message.chat.id, 'دیگه چیکار میتونم برات بکنم؟')


def reffral_handler(message: types.Message):
    reffral_menu = types.ReplyKeyboardMarkup(row_width=1)
    my_reffrals_btn = types.KeyboardButton('♻️ دریافت لینک عضوگیر ی من ♻️')
    reffral_info_btn = types.KeyboardButton('📊 آمار عضو گیری من 📊')
    get_gift_btn = types.KeyboardButton('🎁 دریافت هدیه 🎁')
    reffral_menu.add(reffral_info_btn)
    reffral_menu.add(my_reffrals_btn)
    reffral_menu.add(get_gift_btn)

    back = types.KeyboardButton('🏠')
    reffral_menu.add(back)
    bot.send_photo(
        message.chat.id, 'https://user-images.githubusercontent.com/93007857/201426304-c45ff9f1-f423-453b-8d13-8448357972b0.png', '''تو این وضعیت بد اقتصادی خیلی ها وسع خرید رو ندارن 🤕 ! تیم ما به عشق شما این بخش رو اضافه کرد تا بتونید بدون پرداخت هیچ پولی سرور اختصاصی دریافت کنید 🤠❤️‍🔥

اینجا میتونی از دوست ها و آشناهات دعوت کنی که به خانواده ما بپیوندن، برای دعوت روی < لینک من > کلیک کن ❣️''', reply_markup=reffral_menu)


def my_link_handler(message: types.Message):
    msg = bot.send_photo(
        message.chat.id,
        'https://user-images.githubusercontent.com/93007857/206896123-506f8b37-801e-460d-bca4-c7ded402d85b.png',
        template.create_banner_template(message.chat.id)
    )
    bot.reply_to(msg, template.create_invite_link_inform_template())


def my_points_handler(message: types.Message):
    user = db.get_user(message.chat.id)
    bot.send_message(
        message.chat.id,
        f'🔗 تعداد افراد عضو شده با لینک شما : {user.points}'
    )


def my_gift_handler(message: types.Message):
    gift_menu = types.ReplyKeyboardMarkup()
    five_points_btn = types.KeyboardButton('🥉 هدیه 5 امتیازی 🥉')
    twenty_points_btn = types.KeyboardButton('🥈 هدیه 20 امتیازی 🥈')
    thirty_points_btn = types.KeyboardButton('🥇 هدیه 30 امتیازی 🥇 ')
    back = types.KeyboardButton('🏠')
    gift_menu.add(five_points_btn)
    gift_menu.add(twenty_points_btn)
    gift_menu.add(thirty_points_btn)
    gift_menu.add(back)
    bot.send_message(
        message.chat.id, 'لطفا هدیه مورد نظر خود را انتخاب کنید:', reply_markup=gift_menu
    )


def have_enough_points(user_points, needed_points):
    return True if user_points >= needed_points else False


def not_enough_points(message):
    bot.send_message(
        message.chat.id, 'متاسفم 😕 امتیازهات کافی نیستن !')
    what_else_home_handler(
        message.chat.id, 'دیگه چیکار میتونم برات بکنم؟')


def get_gift_handler(message: types.Message):
    if message.text.lower() == '🏠' or message.text.lower() == '/start':
        what_else_home_handler(message.chat.id, 'برگشت به صفحه اصلی')
        return
    user = db.get_user(message.chat.id)
    if message.text == '🥉 هدیه 5 امتیازی 🥉':
        if have_enough_points(user.points, 5):
            db.decrease_points(user.tel_id, 5)
            bot.send_message(
                message.chat.id, template.create_gift_template(message.text))
            what_else_home_handler(
                message.chat.id, 'دیگه چیکار میتونم برات بکنم؟')
        else:
            not_enough_points(message)
    if message.text == '🥈 هدیه 20 امتیازی 🥈':
        if have_enough_points(user.points, 20):
            db.decrease_points(user.tel_id, 20)
            bot.send_message(
                message.chat.id, template.create_gift_template(message.text))
            what_else_home_handler(
                message.chat.id, 'دیگه چیکار میتونم برات بکنم؟')
        else:
            not_enough_points(message)

    if message.text == '🥇 هدیه 30 امتیازی 🥇':
        if have_enough_points(user.points, 30):
            db.decrease_points(user.tel_id, 30)
            bot.send_message(
                message.chat.id, template.create_gift_template(message.text))
            what_else_home_handler(
                message.chat.id, 'دیگه چیکار میتونم برات بکنم؟')
        else:
            not_enough_points(message)


def invite_handler(message: types.Message, inviter_id):
    db.post_user(message.chat.id, message.chat.first_name,
                 message.chat.username)
    db.add_point(inviter_id)
    user = db.get_user(inviter_id)
    bot.send_message(
        inviter_id, f'تبریک ❣️ {message.chat.first_name} با لینک شما به ربات پیوست.\n🔗 تعداد افراد عضو شده با لینک شما : {user.points}'
    )


def explain_send_server_handler(message: types.Message):
    send_menu = types.ReplyKeyboardMarkup(row_width=1)
    send_btn = types.KeyboardButton('🚀 ارسال 🚀')
    back_btn = types.KeyboardButton('🏠')
    send_menu.add(send_btn)
    send_menu.add(back_btn)
    bot.send_message(
        message.chat.id,
        '  با توجه به شرایط فیلترینگ شدید کشور و محدودیت زمانی تیم ما، از طریق این بخش شما عزیزان هم میتونید اگه سرور یا پروکسی سالمی دارید با بقیه به اشتراک بذارید ❤️',
        reply_markup=send_menu)


def enter_send_server_handler(message: types.Message):

    if message.text.lower() == '🏠' or message.text.lower() == '/start':
        what_else_home_handler(message.chat.id, 'برگشت به صفحه اصلی')
        return False
    bot.send_message(message.chat.id,
                     template.create_send_hint_template(), parse_mode='HTML', reply_markup=types.ReplyKeyboardRemove()
                     )
    return True


def post_send_server_handler(message: types.Message):
    try:
        items = message.text.split('*')
        type = Utils().get_type_of_server(items[0].lower())
        server = items[1]
        if type == 'Proxy':
            connect_menu = types.InlineKeyboardMarkup()
            connect_menu.add(types.InlineKeyboardButton(
                "Connect", callback_data=('connect'), url=server))
            bot.send_message(
                1129145429,
                template.create_proxy_template(type, f' از طرف: <a href="t.me/{message.chat.username}">{message.chat.first_name}</a> ❤️'), reply_markup=connect_menu
            )
        else:
            send_menu = types.InlineKeyboardMarkup(row_width=2)
            check_btn = types.InlineKeyboardButton(
                "✅", callback_data='send_server')
            ignore_btn = types.InlineKeyboardButton(
                "❌", callback_data='dont_send_server')

            send_menu.add(check_btn, ignore_btn)

            bot.send_message(
                1129145429,
                template.create_server_template(
                    type, f'<code>{server}</code>', f' از طرف: <a href="t.me/{message.chat.username}">{message.chat.first_name}</a> ❤️'),
                disable_web_page_preview=True,
                reply_markup=send_menu
            )
        bot.reply_to(
            message, ' با تشکر از شما، بعد از تایید مدیریت در کانال نمایش داده میشود ❤️')
        what_else_home_handler(
            message.chat.id, 'دیگه چیکار میتونم برات بکنم؟')
    except Exception as e:
        what_else_home_handler(
            message.chat.id,  'این فرمت معتبر نیست.')
