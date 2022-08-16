from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from main import Ui_MainWindow
from dother import Ui_Dialog
import speedtest
import ctypes
import threading
import psutil
from multiprocessing import cpu_count
import time
import os
from sys_info import Ui_System_info
import wmi
import random
import pyautogui
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils import config as cfg
import emoji
from time import sleep
from os.path import dirname, realpath, join
import telebot

# ПОГОДА

config = cfg.get_default_config()
config['language'] = 'ru'
owm = OWM('1a8ebdc76badeb07c3afe1b7753cbf6c', config)
mgr = owm.weather_manager()
# ПОГОДА

# БОТ
BOT_TOKEN = 'свой'
BOT_INTERVAL = 3
BOT_TIMEOUT = 30
users = [699846741]
chat_id = -634852109
# БОТ

#Уникальная директория 
your_current_app_directory = dirname(realpath(__file__))
your_custom_folder = "docum"
fold = (your_current_app_directory + "\\" + your_custom_folder+"\\")
#Уникальная директория 

#Основное окно
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
ui.password.setReadOnly(True)#Запрет на редактирование
#Основное окно

def generic_password():
    chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    length = ui.lenght_pass.text()
    password = ''
    for i in range(int(length)):
        password += random.choice(chars)
    ui.password.setText(str(password))

def openotherwindow():
    global Dialog
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()

    def speedtestinm():
        global test
        test = speedtest.Speedtest()
        download = test.download()
        upload = test.upload()
        downloads = round(((download/1024)/1024), 1)
        uploads = round(((upload/1024)/1024), 1)
        ui.uploading.setText("Скорость загрузки: " + str(uploads) + " Mb/s")
        ui.downloading.setText("Скорость скачивания: " + str(downloads) + " Mb/s")

    def returnmain():
        Dialog.hide()  # ЗАХЛОПЫВАЕМ ДОЧКУ
        MainWindow.show()  # ПОКАЗЫВАЕМ ОСНОВНОЕ ОКНО
    # ПРИ НАЖАТИИ ФУНКЦИЯ ТАКАЯ ХОП ЧИКА ХОП ЛЯ НА ОСНОВ
    ui.pushButton1.clicked.connect(returnmain)
    ui.btnBrowse.clicked.connect(speedtestinm)


def sys_info():
    global System_info
    System_info = QtWidgets.QDialog()
    ui = Ui_System_info()
    ui.setupUi(System_info)
    ui.os.setText('Версия винды: {0}'.format(os_version))
    ui.cpu.setText('ЦП: {0}'.format(proc_info.Name))
    ui.ram.setText('Оператива: {0} GB'.format(system_ram))
    ui.gc.setText('Видеокарта: {0}'.format(gpu_info.Name))
    System_info.show()
    def returnmain2():
        System_info.hide()
        MainWindow.show()
    ui.go_home1.clicked.connect(returnmain2)

 

def systezxc_info():
    global os_info, proc_info, os_version, gpu_info, system_ram
    computer = wmi.WMI()
    os_info = computer.Win32_OperatingSystem()[0]
    proc_info = computer.Win32_Processor()[0]
    os_version = ' '.join([os_info.Version, os_info.BuildNumber])
    gpu_info = computer.Win32_VideoController()[1]
    system_ram = round(
        float(os_info.TotalVisibleMemorySize) / 1048576)  # KB to GB


def weather_calc():
    mgr = owm.weather_manager()
    city = ui.lineEdit.text()
    observation = mgr.weather_at_place(city)
    w = observation.weather
    temperature = w.temperature('celsius')['temp']
    wind = w.wind().get("speed", 0)
    status = w.detailed_status
    ui.city_da.setText("Температура: " + str(temperature) + " °С")
    ui.wind_da.setText("Скорость ветра: " + str(wind) + " М/с")
    ui.weat_da.setText("Погода: " + str(status))


def cpu_mem():
    while True:
        global totalRam, availRam, ramUsed, ramFree, ramUsages, cpuPer,percent
        totalRam = 1.0
        totalRam = psutil.virtual_memory()[0] * totalRam
        totalRam = 'Всего памяти: ' + \
            str(round(totalRam / (1024 * 1024 * 1024), 2)) + " GB"
        ui.label_total_memory_2.setText(totalRam)

        availRam = 1.0
        availRam = psutil.virtual_memory()[1] * availRam
        availRam = 'Доступно памяти: ' + \
            str(round(availRam / (1024 * 1024 * 1024), 2)) + " GB"
        ui.label_avail_ram.setText(str(availRam))

        ramUsed = 1.0
        ramUsed = psutil.virtual_memory()[3] * ramUsed
        ramUsed = 'Использовано памяти: ' + \
            str(round(ramUsed / (1024 * 1024 * 1024), 2)) + " GB"
        ui.label_ram_used.setText(str(ramUsed))

        ramFree = 1.0
        ramFree = psutil.virtual_memory()[4] * ramFree
        ramFree = 'Свободно: ' + \
            str(round(ramFree / (1024 * 1024 * 1024), 2)) + " GB"
        ui.label_ram_free.setText(str(ramFree))

        core = 'Количество потоков: ' + str(cpu_count())
        ui.label_core.setText(str(core))

        ramUsages = 'Задействовано памяти: ' + \
            str(psutil.virtual_memory()[2]) + ' %'
        ui.label_ram_usages.setText(str(ramUsages))
        #print("Задействовано памяти: ",ramUsages)
        #self.ui.ram_usage.setText(str("{:.4f}".format(totalRam) + ' GB'))

        cpuPer = 'Используется цп: ' + str(psutil.cpu_percent()) + ' %'
        ui.label_cpu_per.setText(str(cpuPer))
        #print("Используется цп: ",cpuPer, "%")
        #self.ui.cpu_per.setText(str(cpuPer) + " %")

        cpuMainCore = 'Количество ядер: ' + \
            str(psutil.cpu_count(logical=False))
        ui.label_cpu_main_core.setText(str(cpuMainCore))

        battery = psutil.sensors_battery()
        percent = int(battery.percent)
        ui.charg_da.setText(f"Заряд батареи: {percent}%")
        time.sleep(1)


def bot_polling():
    # Запускаем бота и вывод состояния бота
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

    @bot.message_handler(commands=["hi"])
    def command_start(message):
        bot.send_message(message.chat.id, "Hi there!")

    @bot.message_handler(commands=['save'])
    def scrin(message):
        pyautogui.screenshot(fold + "screen.png")
        with open(fold + "screen.png", "rb") as screen:
            bot.send_photo(message.chat.id, screen)
            bot.send_photo(message.chat.id, "FILEID")
        screen.close()
    @bot.message_handler(commands=['lock'])
    def winlock(message):
        ctypes.windll.user32.LockWorkStation()
    
    @bot.message_handler(commands=["off"])
    def offline(message):
        os.system('shutdown -s')
    
    @bot.message_handler(commands=["info"])
    def invinfo(message):
        getinfo = str(totalRam) + "\n" + str(availRam) + "\n" + str(ramUsed) 
        + "\n" + str(ramFree) + "\n" + str(ramUsages) 
        + "\n" + str(cpuPer) + "\n" + "Заряд батареи " + str(percent) + "%"
        bot.send_message(message.chat.id, getinfo)

    @bot.message_handler(commands=['weather'])
    def zxcdaa(message):
        bot.send_message(message.chat.id, "Выберите город")

        @bot.message_handler(content_types=['text'])
        def weather_otvet(message):
            city = message.text
            observation = mgr.weather_at_place(city)
            w = observation.weather
            temperature = w.temperature('celsius')['temp']
            wind = w.wind().get("speed", 0)
            status = w.detailed_status
            complete = "В городе сейчас: " + str(temperature) + "°С" "\n" + "Скорость ветра: " + str(
                wind) + " М/с" "\n" "Погода: " + str(status) + emoji.emojize(':pile_of_poo:')
            bot.send_message(message.chat.id, complete)


polling_thread = threading.Thread(target=cpu_mem)
polling_thread.daemon = True
polling_thread.start()

polling_thread = threading.Thread(target=bot_polling)
polling_thread.daemon = True
polling_thread.start()

systezxc_info()

ui.weather_go.clicked.connect(weather_calc)
ui.generic_pass.clicked.connect(generic_password)
ui.speedtestir.clicked.connect(openotherwindow)
ui.sys_info.clicked.connect(sys_info)
sys.exit(app.exec_())

