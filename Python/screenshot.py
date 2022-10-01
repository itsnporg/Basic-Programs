import time
import pyautogui

def screenshot():
    name = int(round(time.time()*1000))
    name = '{}.png'
    time.sleep(5)
    img = pyautogui.screenshot(name)
    img.show()

screenshot()
