import os
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, ChatJoinRequestHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")

IT_KEYWORDS = ["IT", "INFORMATION TECHNOLOGY"]
GREETING_MESSAGES = [
    "{name} ရေ ကျန်းမာရေးဂရုစိုက်ပါ",
    "{name} ရေ ကြိုးစားပါ",
    "{name} ရေ မင်းအတွက်အနာဂတ်ကောင်းတယ်",
    "{name} ရေ စိတ်ချမ်းသာစွာနေနိုင်ပါစေ",
    "{name} ရေ မေတ္တာတွေနဲ့ပြည့်စေပါစေ",
    "{name} ရေ နေ့တိုင်းမောင်္မာကြွယ်ဝပါစေ"
]

async def approve_if_it(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.chat_join_request.from_user
    chat = update.chat_join_request.chat
    bio_upper = (user.bio or "").upper()
    full_name = user.full_name

    if any(keyword in bio_upper for keyword in IT_KEYWORDS):
        await context.bot.approve_chat_join_request(chat_id=chat.id, user_id=user.id)
        message = random.choice(GREETING_MESSAGES).format(name=full_name)
        await context.bot.send_message(chat_id=chat.id, text=f"{full_name} ကို ဝင်ခွင့်ပြုလိုက်ပါတယ်။\n{message}")
    else:
        await context.bot.decline_chat_join_request(chat_id=chat.id, user_id=user.id)
        await context.bot.send_message(chat_id=chat.id, text=f"{full_name} Bio မှာ IT မပါလို့ ဝင်ခွင့်မပြုပါ။")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(ChatJoinRequestHandler(approve_if_it))
app.run_polling()
