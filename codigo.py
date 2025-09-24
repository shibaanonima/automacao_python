import pyautogui
import time

# abrir gogle chrome

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(0.5)
pyautogui.write("http://127.0.0.1:5500/index.html")
pyautogui.press("enter")
time.sleep(1)
pyautogui.moveTo(x=1054, y=442)
pyautogui.click(x=1054, y=442)
pyautogui.write("sofia")
pyautogui.press("tab")
time.sleep(1)
pyautogui.moveTo(x=1010, y=528)
pyautogui.click(x=1010, y=528)
pyautogui.write("sofia123@gmail.com")
pyautogui.press("tab")
time.sleep(1)
pyautogui.moveTo(x=1030, y=596)
pyautogui.click(x=1030, y=596)
pyautogui.write("sla12341")
pyautogui.press("tab")
time.sleep(1)
pyautogui.moveTo(x=888, y=717)
pyautogui.press("enter")


