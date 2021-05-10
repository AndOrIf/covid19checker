import COVID19Py
import telebot
from telebot import types

covid19 = COVID19Py.COVID19()
bot = telebot.TeleBot('1712771971:AAGmZHnqfTk6pPvnHroqcRP-Egj7F24iLWk')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    bt1 = types.KeyboardButton("Мир")
    bt2 = types.KeyboardButton("Россия")
    bt3 = types.KeyboardButton("Украина")
    bt4 = types.KeyboardButton("Казахстан")
    bt5 = types.KeyboardButton("Индия")
    bt6 = types.KeyboardButton("США")
    bt7 = types.KeyboardButton("Белоруссия")
    markup.add(bt1, bt2, bt3, bt4, bt5, bt6, bt7)
    send_mess = f"<b>Здравствуйте, {message.from_user.first_name}!</b>\nВыбирете страну"
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def mess(message):
    final_message = ""
    get_message_bot = message.text.strip().lower()
    if get_message_bot == "сша":
        location = covid19.getLocationByCountryCode("US")
    elif get_message_bot == "украина":
        location = covid19.getLocationByCountryCode("UA")
    elif get_message_bot == "россия":
        location = covid19.getLocationByCountryCode("RU")
    elif get_message_bot == "казахстан":
        location = covid19.getLocationByCountryCode("KZ")
    elif get_message_bot == "белоруссия":
        location = covid19.getLocationByCountryCode("BY")
    elif get_message_bot == "индия":
        location = covid19.getLocationByCountryCode("IN")
    elif get_message_bot == "мир":
        location = covid19.getLatest()
        final_message = f"<u>Данные по всему миру:</u>\n"\
                        f"<b>Зараженных: </b>{location['confirmed']}\n<b>Выздоровело: </b>{location['recovered']}\n<b>Умерло: </b>{location['deaths']}"
    else:
        final_message = "Я не понял вашу команду"


    if final_message == "":
        date = location[0]['last_updated'].split("T")
        time = date[1].split(".")
        final_message = f"<u>Данные по стране:</u>\nНаселение: {location[0]['country_population']} человек(а)\n"\
                        f"<b>Последнее обновление:</b> {date[0]} {time[0]}\n"f"<u>Последние данные:</u>\n"\
                        f"<b>Зараженных: </b> {location[0]['latest']['confirmed']:,} человек(а)\n"\
                        f"<b>Умерло: </b> {location[0]['latest']['deaths']:,} человек(а)"



    bot.send_message(message.chat.id, final_message, parse_mode = 'html')



bot.polling(none_stop=True)