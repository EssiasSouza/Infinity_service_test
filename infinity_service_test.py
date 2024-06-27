import pyautogui
import time

pyautogui.FAILSAFE = False

def enchamba():
    while True:
        pyautogui.press('shift')
        time.sleep(60)

if __name__ == "__main__":
    enchamba()