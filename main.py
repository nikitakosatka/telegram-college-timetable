import telebot
from time import sleep
from datetime import datetime

from key import token

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id,
                     "Введите время, в которое будет приходить расписние, в виде hh:mm",
                     parse_mode="Markdown")


@bot.message_handler(content_types=['text'])
def get_indicated_time(message):
    try:
        indicated_time = message.text
        if not is_correct_time(indicated_time):
            raise ValueError

        indicated_time = ':'.join(map(str, (map(int, indicated_time.split(':')))))

        text = f"Время выбрано. Расписание придет в {indicated_time}"
        bot.send_message(message.chat.id, text, parse_mode="Markdown", reply_markup=None)

        while True:
            send_notice(message.chat.id, indicated_time)
            sleep(60)

    except ValueError:
        bot.send_message(message.chat.id,
                         "Ошибка, введите время в виде hh:mm",
                         parse_mode="Markdown")


def send_notice(chat_id, indicated_time):
    if indicated_time == str(datetime.now().hour) + str(datetime.now().minute):
        text = "test"
        bot.send_message(chat_id, text, parse_mode="Markdown")


def is_correct_time(time):
    new_time = time.split(':')
    if len(new_time) == 2:
        if int(new_time[0]) in range(0, 24) and int(new_time[1]) in range(0, 60):
            return True

    return False


bot.polling(none_stop=True, interval=0)
