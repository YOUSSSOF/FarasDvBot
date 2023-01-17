from telebot import TeleBot
from utils import Utils

channel_id = Utils().get_channel_id()
api_key: str = Utils().get_api_key()
bot = TeleBot(api_key)
server_base_url = ':8000'
