import pyautogui
import time
import keyboard
import threading


def clickaem_po_popkam():
    while True:
        while keyboard.is_pressed("alt+v"):
            time.sleep(0.05)
            pyautogui.click()
clickaem_po_popkam()

