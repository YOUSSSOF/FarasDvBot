from .base import KeyBoardBase
from telebot import types


class AdminKeyBoard(KeyBoardBase):

    def __init__(self):
        super().__init__()
        self.main_admin_menu = types.ReplyKeyboardMarkup(row_width=2)
        post_server_btn = types.KeyboardButton('➕ Post a new server ➕')
        post_infrom_btn = types.KeyboardButton('❗ Post a new infrom ❗')
        message_all_membders_btn = types.KeyboardButton(
            '✉️ Message members ✉️')
        list_all_membders_btn = types.KeyboardButton(
            '📋 List members 📋')
        edit_sponsers_btn = types.KeyboardButton(
            '✏️ Edit Sponsers ✏️')
        user_menu_btn = types.KeyboardButton('🧍🏻‍♂️ Go to user menu 🧍🏻‍♂️')
        self.main_admin_menu.add(post_server_btn, post_infrom_btn)
        self.main_admin_menu.add(
            message_all_membders_btn, list_all_membders_btn)
        self.main_admin_menu.add(edit_sponsers_btn)
        self.main_admin_menu.add(user_menu_btn)
