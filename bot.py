import telebot
from telebot import types

TOKEN = "8335187940:AAFsn3H2MjbseinmVxZKCHC9aJfRyRYST4c"

bot = telebot.TeleBot(TOKEN)

schedule = {
    "Dushanba": "📚 *Dushanba*\n\n📌 10:00 – 11:20\n📘 Moliyaviy tahlil (Ma)\n\n━━━━━━━━━━━━━━━━━━━━\n📌 13:30 – 14:50\n📘 Ekonometrika (Ma)",
    "Seshanba": "📚 *Seshanba*\n\n📌 10:00 – 11:20\n📘 Pul va kredit 2 (Ma)",
    "Chorshanba": "📚 *Chorshanba*\n\n📌 10:00 – 11:20\n📘 Investitsiya loyihalarini moliyalashtirish (Ma)",
    "Payshanba": "📚 *Payshanba*\n\n📌 15:00 – 16:20\n📘 Banklarda buxgalteriya hisobi 1 (Ma)",
    "Juma": "📚 *Juma*\n\n📌 13:30 – 14:50\n📘 Makroiqtisodiyot I (Ma)"
}

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Dushanba", "Seshanba")
    markup.add("Chorshanba", "Payshanba")
    markup.add("Juma")

    bot.send_message(
        message.chat.id,
        "📅 Kunni tanlang:",
        reply_markup=markup
    )

@bot.message_handler(func=lambda m: m.text in schedule)
def show_day(message):
    bot.send_message(
        message.chat.id,
        schedule[message.text],
        parse_mode="Markdown"
    )

bot.infinity_polling()
