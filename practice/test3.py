import pyautogui
import time, sys

# for w in pyautogui.getAllWindows():
#     print(w)

# w = pyautogui.getWindowsWithTitle("Pushbullet - Your devices working better together - Chrome")[0]

# if w.isActive == False:
#     w.activate()

# "특가대표! 위메프 - Chrome"
# pyautogui.sleep(5)
# CertNumber = pyautogui.locateOnScreen("C:/python study/selenium/CertificationNumber.png", confidence=0.8)
# pyautogui.click(CertNumber)

# pyautogui.mouseInfo()
# 1514,782 249,249,249 #F9F9F9
# 1915,1045 112,112,112 #707070

CertNumberSend = pyautogui.locateOnScreen("C:/python study/selenium/CertificationNumberSend.png", region=(1514, 782, 401, 263))

def find_target(img_file, timeout=30):
    start = time.time()
    target = None
    while target is None:
        target = pyautogui.locateOnScreen(img_file)
        end = time.time()
        if end - start > timeout:
            break
    return target

def my_click(img_file, timeout=30):
    target = find_target(img_file, timeout)
    if target:
        pyautogui.click(target)
    else:
        print("f[timeout {timeout}s] Target not found ({img_file}).")

my_click("C:/python study/selenium/CertificationNumberSend.png", 30)