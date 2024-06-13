import pyautogui
import time

# Function to scroll down
def scroll_down(amount):
    pyautogui.scroll(-amount)

# Function to scroll up
def scroll_up(amount):
    pyautogui.scroll(amount)

# Example usage
if __name__ == "__main__":
    # Scroll down 10 "clicks"
    scroll_down(10)
    time.sleep(2)
    
    # Scroll up 5 "clicks"
    scroll_up(5)
