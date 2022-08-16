import pyautogui
import time
import keyboard


def clickaem():
    while True:
        while keyboard.is_pressed("alt+v"):
            time.sleep(0.05)
            pyautogui.click()
clickaem()

