from dotenv import load_dotenv
import config
import os

servers = [
    'V2ray', 'Argo Bridge', 'Argo Falcon',
    'ShadowSocks', 'Brook', 'Outline', 'Proxy'
]


class Utils:
    def get_api_key(self):
        load_dotenv()
        return os.environ.get('API')

    def get_channel_id(self):
        load_dotenv()
        return int(os.environ.get('CHANNEL'))

    def get_admins(self):
        return int(os.environ.get('ADMIN_1')), int(os.environ.get('ADMIN_2'))

    def is_admin(self, id):
        if id in self.get_admins():
            return True
        return False

    def get_type_of_server(self, link: str):

        if link == 'v2':
            return servers[0]
        elif link == 'ab':
            return servers[1]
        elif link == 'af':
            return servers[2]
        elif link == 'ss':
            return servers[3]
        elif link == 'b':
            return servers[4]
        elif link == 'o':
            return servers[5]
        elif link == 'mp':
            return servers[6]
        else:
            return 'Unknown'

    def is_in_channel(self, id, bot):
        try:
            con = bot.get_chat_member(config.channel_id, id)
            if con.status == 'left':
                return False
            return True

        except:
            return False
