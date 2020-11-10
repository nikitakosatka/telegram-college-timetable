import telebot
from time import sleep
from datetime import datetime

from key import token
from excel_parser import get_day_timetable

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id,
                     "Введите время, в которое будет приходить расписание, в виде hh:mm",
                     parse_mode="Markdown")


@bot.message_handler(content_types=['text'])
def get_indicated_time(message):
    try:
        indicated_time = message.text
        if not is_correct_time(indicated_time):
            raise ValueError

        indicated_time = ':'.join(map(str, (map(int, indicated_time.split(':')))))

        text = f"Время выбрано. Расписание придет в {indicated_time.split(':')[0]}ч. {indicated_time.split(':')[1]}м."
        bot.send_message(message.chat.id, text, parse_mode="Markdown", reply_markup=None)

        was_sent = False

        while True:
            if indicated_time == f"{str(datetime.now().hour)}:{str(datetime.now().minute)}":
                send_notice(message.chat.id, was_sent)
                was_sent = True
            else:
                was_sent = False

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

        text = get_day_timetable(datetime.today().weekday() + 1, is_odd)
        bot.send_message(chat_id, text, parse_mode="Markdown")


def is_correct_time(time):
    new_time = time.split(':')
    if len(new_time) == 2:
        if int(new_time[0]) in range(0, 24) and int(new_time[1]) in range(0, 60):
            return True

    return False
