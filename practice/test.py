import pyautogui as py
import time

# py.mouseInfo()

time.sleep(5)
py.click(1000, 15)
while True:
	loc = 135
	for i in range(39):
		py.click(1077, loc)
		py.hotkey('ctrl','c')
		py.doubleClick(450, 60)
		py.hotkey('ctrl','v')
		py.hotkey('enter')
		py.doubleClick(1700, 215)
		py.hotkey('ctrl','v')
		py.hotkey('backspace')
		py.hotkey('enter')
		loc = loc + 22
		time.sleep(2)
		py.click(1000, 15)
	py.scroll(-1650)