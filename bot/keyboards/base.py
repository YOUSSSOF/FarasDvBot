from telebot import types


class KeyBoardBase:
    def __init__(self):
        self.back_menu = types.ReplyKeyboardMarkup(row_width=1)
        back = types.KeyboardButton('🏠')
        self.back_menu.add(back)
