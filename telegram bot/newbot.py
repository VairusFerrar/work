from email import message
import telebot
import threading
from time import sleep
import pyautogui
import PIL
from os.path import dirname, realpath, join
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
import emoji
from pyowm.utils import config as cfg
from telebot import types
#Бот
BOT_TOKEN = 'secret'
BOT_INTERVAL = 3
BOT_TIMEOUT = 30
users = [ 699846741 ]
chat_id = -634852109
#Бот
#Динамичный путь
your_current_app_directory = dirname(realpath(__file__))
your_custom_folder = "docum"
fold = (your_current_app_directory + "\\" + your_custom_folder+"\\")
#Динамичный путь

 #ИД группы

#Погода
config = cfg.get_default_config()
config['language'] = 'ru'
owm = OWM('1a8ebdc76badeb07c3afe1b7753cbf6c', config)
mgr = owm.weather_manager()
#Погода

################################################НАЧИНАЕМ КОДИТЬ##################################################################
################################################НАЧИНАЕМ КОДИТЬ##################################################################
################################################НАЧИНАЕМ КОДИТЬ##################################################################
def bot_polling():
    #Запускаем бота и вывод состояния бота
    print("Запуск бота")
    while True:
        try:
            print("Начат прием запросов")
            bot = telebot.TeleBot(BOT_TOKEN)
            botactions(bot)
            bot.polling(none_stop=True, interval=BOT_INTERVAL,
                        timeout=BOT_TIMEOUT)
        except Exception as ex:  # Error in polling
            print("Ошибка бота, перезапуск через {}sec. Error:\n{}".format(
                BOT_TIMEOUT, ex))
            bot.stop_polling()
            sleep(BOT_TIMEOUT)
        else:  # Clean exit
            bot.stop_polling()
            print("Завершение приема запроса")
            break  # Выход


def botactions(bot):
    @bot.message_handler(func=lambda message: message.from_user.id not in users)
    def some(message):
        bot.send_message(message.chat.id, 'Коля ебалай')
          
    @bot.message_handler(commands=["hi"])
    def command_start(message):
        bot.send_message(message.chat.id, "Hi there!")

    @bot.message_handler(commands=['get'])
    def getdoc(message):
        with open(fold + "bot.rar", "rb") as new_file:
            bot.send_document(message.chat.id, new_file)
            bot.send_document(message.chat.id, "FILEID")
        new_file.close()

    @bot.message_handler(commands=['save'])
    def scrin(message):
        pyautogui.screenshot(fold + "screen.png")
        with open(fold + "screen.png", "rb") as screen:
            bot.send_photo(message.chat.id, screen)
            bot.send_photo(message.chat.id, "FILEID")
        screen.close()

    @bot.message_handler(commands=['weather'])
    def zxcdaa(message):
        bot.send_message(message.chat.id, "Выберите город")
        @bot.message_handler(content_types=['text'])
        def weather_otvet(message):           
            city = message.text
            observation = mgr.weather_at_place(city)
            w = observation.weather
            temperature = w.temperature('celsius')['temp']
            wind = w.wind().get("speed",0)
            status = w.detailed_status
            complete="В городе сейчас: " + str(temperature) + "°С" "\n" + "Скорость ветра: " + str(wind)+ " М/с" "\n" "Погода: " + str(status) + emoji.emojize(':pile_of_poo:')
            bot.send_message(message.chat.id, complete)

polling_thread = threading.Thread(target=bot_polling)
polling_thread.daemon = True
polling_thread.start()
    

#Сохраняет окно программы пока бот в потоке
if __name__ == "__main__":
    while True:
        try:
            sleep(120)
        except KeyboardInterrupt:
            break
"""
keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes'); #кнопка «Да»
keyboard.add(key_yes); #добавляем кнопку в клавиатуру
key_no= types.InlineKeyboardButton(text='Нет', callback_data='no');
keyboard.add(key_no);
"""
