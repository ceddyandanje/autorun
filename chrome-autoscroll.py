import pyautogui
import psutil
import time


def scroll_down(amount):
    pyautogui.scroll(-amount)


def scroll_up(amount):
    pyautogui.scroll(amount)


def is_chrome_running():
    for process in psutil.process_iter(['name']):
        if 'chrome' in process.info['name'].lower():
            return True
    return False


if __name__ == "__main__":
    while True:
        if is_chrome_running():
            print("Chrome is running, scrolling down.")
            scroll_down(10) 
            time.sleep(2)  
        else:
            print("Chrome is not running, waiting.")
            time.sleep(3)  
