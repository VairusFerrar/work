import psutil
from multiprocessing import cpu_count
import time
import os
def cpu_mem():
    while True:
        totalRam = 1.0
        totalRam = psutil.virtual_memory()[0] * totalRam
        totalRam = 'Всего памяти: ' + \
            str(round(totalRam / (1024 * 1024 * 1024), 2)) + " GB"
        print(totalRam)

        availRam = 1.0
        availRam = psutil.virtual_memory()[1] * availRam
        availRam = 'Доступно памяти: ' + \
            str(round(availRam / (1024 * 1024 * 1024), 2)) + " GB"
        print(str(availRam))

        ramUsed = 1.0
        ramUsed = psutil.virtual_memory()[3] * ramUsed
        ramUsed = 'Использовано памяти: ' + \
            str(round(ramUsed / (1024 * 1024 * 1024), 2)) + " GB"
        print(str(ramUsed))

        ramFree = 1.0
        ramFree = psutil.virtual_memory()[4] * ramFree
        ramFree = 'Свободно: ' + \
            str(round(ramFree / (1024 * 1024 * 1024), 2)) + " GB"
        print(str(ramFree))

        core = 'Количество потоков: ' + str(cpu_count())
        print(str(core))

        ramUsages = 'Задействовано памяти: ' + \
            str(psutil.virtual_memory()[2]) + ' %'
        print(str(ramUsages))
        #print("Задействовано памяти: ",ramUsages)
        #self.ui.ram_usage.setText(str("{:.4f}".format(totalRam) + ' GB'))

        cpuPer = 'Используется цп: ' + str(psutil.cpu_percent()) + ' %'
        print(str(cpuPer))
        #print("Используется цп: ",cpuPer, "%")
        #self.ui.cpu_per.setText(str(cpuPer) + " %")

        cpuMainCore = 'Количество ядер: ' + \
            str(psutil.cpu_count(logical=False))
        print(str(cpuMainCore))

        battery = psutil.sensors_battery()
        percent = int(battery.percent)
        print(f"Заряд батареи: {percent}%")
        time.sleep(1)
        os.system("cls")

cpu_mem()