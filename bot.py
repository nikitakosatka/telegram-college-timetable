import telebot

from key import token
from excel_parser import get_this_week_consultation_info, get_full_consultation_info

bot = telebot.TeleBot(token)

custom_keyboard = [['top-left', 'top-right'],
                   ['bottom-left', 'bottom-right']]


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id,
                     "Введите фамилию преподавателя, который ведет консультации",
                     parse_mode="Markdown")


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id,
                     "Введите фамилию преподавателя, который ведет консультации, чтобы получить расписание консультаций\n"
                     "Чтобы получить ближайшую консультацию, введите: \"Фамилия преподавателя\" б/ближайшая",
                     parse_mode="Markdown")


@bot.message_handler(content_types=['text'])
def send_message(message):
    try:
        surname = message.text.split()[0][0].upper() + message.text.split()[0][1:].lower()
        if message.text.split()[-1].lower() in ['ближайшая', 'б', '1']:
            text = get_this_week_consultation_info(surname)
        else:
            text = get_full_consultation_info(surname)
        bot.send_message(message.chat.id, text, parse_mode="Markdown")

    except KeyError:
        bot.send_message(message.chat.id, "Преподаватель не найден. Введите фамилию еще раз",
                         parse_mode="Markdown")
