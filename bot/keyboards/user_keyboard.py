from .base import KeyBoardBase
from telebot import types


class UserKeyBoard(KeyBoardBase):
    def __init__(self):
        super().__init__()
        self.main_user_menu = types.ReplyKeyboardMarkup(row_width=2)
        new_proxies_btn = types.KeyboardButton('🕊️ جدیدترین پروکسی ها 🕊️')
        send_server_btn = types.KeyboardButton('💯 ارسال سرور  💯')
        reffral_btn = types.KeyboardButton('🎰 دریافت سرور اختصاصی رایگان 🎰')
        contact_us_btn = types.KeyboardButton('💌 ارتباط با ما 💌')
        self.main_user_menu.add(new_proxies_btn)
        self.main_user_menu.add(send_server_btn, contact_us_btn)
        self.main_user_menu.add(reffral_btn)
