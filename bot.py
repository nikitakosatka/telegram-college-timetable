import telebot
from datetime import datetime

from key import token
from excel_parser import get_consultation_info

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id,
                     "Введите время, в которое будет приходить расписание, в виде hh:mm",
                     parse_mode="Markdown")


@bot.message_handler(content_types=['text'])
def get_indicated_time(message):
    try:
        text = get_consultation_info(message.text)
        bot.send_message(message.chat.id, text, parse_mode="Markdown")

    except ValueError:
        bot.send_message(message.chat.id,
                         "Ошибка, введите время в виде hh:mm",
                         parse_mode="Markdown")


def send_notice(chat_id, was_sent):
    if not was_sent:
        if datetime.today().isocalendar()[1] + 1 % 2 == 0:
            is_odd = False
        else:
            is_odd = True

        text = get_consultation_info(datetime.today().weekday() + 1, is_odd)
        bot.send_message(chat_id, text, parse_mode="Markdown")


def is_correct_time(time):
    new_time = time.split(':')
    if len(new_time) == 2:
        if int(new_time[0]) in range(0, 24) and int(new_time[1]) in range(0, 60):
            return True

    return False
