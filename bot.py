import telebot
from datetime import datetime

TOKEN = "8335187940:AAFsn3H2MjbseinmVxZKCHC9aJfRyRYST4c"

bot = telebot.TeleBot(TOKEN)

schedule = {
    "monday": "📘 Ekonometrika",
    "tuesday": "📕 Pul Va Kredit",
    "wednesday": "📘 Investitsiya",
    "thursday": "📕 Banklarda bugxalteriya",
    "friday": "📙 Makroiqtisodiyot"
}

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Salom! /today yoz — bugungi darslar chiqadi")

@bot.message_handler(commands=['today'])
def today(message):
    day = datetime.now().strftime("%A").lower()
    bot.reply_to(message, schedule.get(day, "Bugun dars yo‘q 🙂"))

bot.infinity_polling()