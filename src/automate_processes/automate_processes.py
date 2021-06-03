import pyautogui
import time
import pyperclip

pyautogui.PAUSE = 1
#abrir navegador
'''
pyautogui.press("winleft")
pyautogui.write("Google Chrome")
pyautogui.press("enter")
'''

pyautogui.alert("Vai começar, aperte OK e não mexa em nada")
pyautogui.hotkey("ctrl", "t")

link="https://drive.google.com/drive/u/0/folders/1UWrsc-BnO6JMOReOzuyqEpMZ1uzU-Nsq"
pyperclip.copy(link)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
time.sleep(15)

pyautogui.position(317, 273, clicks=2)
pyautogui.position(398, 274)
pyautogui.position(1695, 170)
pyautogui.position(1622, 616)
time.sleep(10)