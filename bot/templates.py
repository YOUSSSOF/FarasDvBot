class Template:
    def create_server_template(self, type: str, server: str, is_from: str = ''):
        return f'''🔥 سرور {type} جدید.

{server}

با یک ضربه بر روی سرور موردنظر، آن را کپی کنید❗

{is_from}
🕊️ Join us: @FarasDvVpn
#{'_'.join(type.lower().split(' '))}
'''

    def create_proxy_template(self, type: str, is_from: str = '', location=''):
        return f'''🔥 سرور {type} جدید.

{is_from if is_from else location}
🕊️ Join us: @FarasDvVpn
#{'_'.join(type.lower().split(' '))}
'''

    def create_inform_template(self, message: str):
        return f'''❗ اطلاعیه

{message}

🕊️ Join us: @FarasDvVpn
'''

    def create_reffral_template(self, user: str):
        return f'''{user} عزیز

🟡 به ازای هر ۵ نفر ⬅️
« ۵ » گیگابایت اشتراک رایگان 📥
از سرور اختصاصی و پر سرعت ما 💥

🟠 به ازای هر ۲۰ نفر ⬅️
« ۱۵ » گیگابایت اشتراک رایگان 📥
از سرور اختصاصی و پر سرعت ما 💥

🔴 به ازای هر ۳۰ نفر ⬅️
« ۲۰ » گیگابایت اشتراک رایگان 📥
از سرور اختصاصی و پر سرعت ما 💥

برای گرفتن لینک اختصاصی خود گزینه لینک من را کلیک کنید ✅
'''

    def create_send_hint_template(self):
        return '''
لطفا سرور خود را در فرمت زیر وارد کنید :

❗ <code>server_type*server_link</code>


نکته: لیست سرور های پشتیبانی شده و فرمت هایشان👇

🟢 V2ray: v2
🟢 Argo Bridge: ab
🟢 Argo Falcon: af
🟢 ShadowSocks: ss
🟢 Brook: b
🟢 Outline: o
🟢 Proxy: mp


نمونه ارسال:

v2*vmess://serverlink
'''

    def create_invite_link_inform_template(self):
        return '''
لینک⚡️ دعوت شما با موفقیت ساخته شد 👆

شما میتوانید بنر حاوی لینک خود را به گـــروه ها و دوستان خود ارسال کنید.
- با معرفی هر نفر 1 امتیاز بگیرید !
'''

    def create_banner_template(self, id):
        return f''' ❣️ فراس دی وی❣️
از قطعی اینترنت وسط چت، گیم، وبگردی خسته شدی؟! خب بیا اینجا vpn مفتی بگیر😳❤️‍🔥
 حتما میپرسی مگه هنوزم چیز مفتی پیدا میشه؟ 🫣
ما داخل کانالمون سرورها و پروکسی های پرسرعت رو به صورت لحظه ای قرار میدیم 🫡 حتی سرور اختصاصی رایگان هم داخل رباتمون بهت میدیم ! دیگه چی میخوای ؟ 😂😂
همین الان وارد ربات شو تا از دستت نرفته، از من گفتن بود🙆‍♂️

http://t.me/FarasDvBot?start={id}'''

    def create_gift_template(self, gift):
        return f'''تبریک❗برای دریافت {gift} خود از همین پیام برای پشتیبانی یک اسکرین شات ارسال کنید 😇

support 👉 @FarasDvSupport'''
