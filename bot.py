import telebot

from key import token
from excel_parser import get_consultation_info

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id,
                     "Введите фамилию преподавателя, который ведет консультации",
                     parse_mode="Markdown")


@bot.message_handler(content_types=['text'])
def send_message(message):
    try:
        surname = message.text[0].upper() + message.text[1:].lower()
        text = get_consultation_info(surname)
        bot.send_message(message.chat.id, text, parse_mode="Markdown")

    except KeyError:
        bot.send_message(message.chat.id, "Преподаватель не найден. Введите фамилию еще раз",
                         parse_mode="Markdown")
