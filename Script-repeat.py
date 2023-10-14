import pyautogui
import time
# Get the number of times you want to repeat the message
num_repeats = 5

time.sleep(3)
for i in range(num_repeats):
    pyautogui.write("hola")
    pyautogui.press("enter")
 pip install pyautogui
