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
    indicated_time = message.text

    text = f"Время выбрано. Расписание придет в {indicated_time}"
    chat_id = message.chat.id
    bot.send_message(chat_id, text, parse_mode="Markdown", reply_markup=None)

    while True:
        send_notice(chat_id, indicated_time)
        time.sleep(60)


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
