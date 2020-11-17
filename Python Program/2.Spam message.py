import pyautogui
import time
time.sleep(20)
for i in range(100):
    for j in range (10):
        pyautogui.press("s")
        pyautogui.press("p")
        pyautogui.press("a")
        pyautogui.press("m")
        pyautogui.press(" ")
    pyautogui.press("enter")
