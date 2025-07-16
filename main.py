from telegram.ext import Updater, ChatJoinRequestHandler
import random

BOT_TOKEN = "7639839035:AAGgsOb_P7gmIssQEuYLXYLQEWpE4oxIlgo"

IT_KEYWORDS = ["IT", "INFORMATION TECHNOLOGY"]

GREETING_MESSAGES = [
    "{name} ရေ ကျန်းမာရေးဂရုစိုက်ပါ",
    "{name} ရေ ကြိုးစားပါ",
    "{name} ရေ မင်းအတွက်အနာဂတ်ကောင်းတယ်",
    "{name} ရေ စိတ်ချမ်းသာစွာနေနိုင်ပါစေ",
    "{name} ရေ မေတ္တာတွေနဲ့ပြည့်စေပါစေ",
    "{name} ရေ နေ့တိုင်းမောင်္မာကြွယ်ဝပါစေ"
]

def approve_if_it(update, context):
    user = update.chat_join_request.from_user
    chat = update.chat_join_request.chat
    bio = user.bio or ""
    full_name = user.full_name
    bio_upper = bio.upper()

    if any(keyword in bio_upper for keyword in IT_KEYWORDS):
        context.bot.approve_chat_join_request(chat_id=chat.id, user_id=user.id)

        message_template = random.choice(GREETING_MESSAGES)
        message = message_template.format(name=full_name)

        context.bot.send_message(
            chat_id=chat.id,
            text=f"{full_name} ကို ဝင်ခွင့်ပြုလိုက်ပါတယ်။\n{message}"
        )
    else:
        context.bot.decline_chat_join_request(chat_id=chat.id, user_id=user.id)
        context.bot.send_message(
            chat_id=chat.id,
            text=f"{full_name} Bio မှာ IT မပါလို ဝင်ခွင့်မပြုပါ။"
        )

updater = Updater(BOT_TOKEN, use_context=True)
updater.dispatcher.add_handler(ChatJoinRequestHandler(approve_if_it))

updater.start_polling()
updater.idle()

