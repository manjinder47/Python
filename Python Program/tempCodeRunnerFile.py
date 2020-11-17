import pyautogui
import webbrowser as wb
import time
wb.open("web.whatsapp.com")
time.sleep(45)
for i in range(20):
    pyautogui.press("hello")
