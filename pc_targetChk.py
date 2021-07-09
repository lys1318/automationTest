import time
import pyautogui as py

def find_target(img_file, timeout=30):
    start = time.time()
    target = None
    while target is None:
        target = py.locateOnScreen(img_file)
        end = time.time()
        if end - start > timeout:
            break
    return target

def my_click(img_file, timeout=30):
    target = find_target(img_file, timeout)
    if target:
        pass
    else:
        print("f[timeout {timeout}s] Target not found ({img_file}).")