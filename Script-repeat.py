import pyautogui
import time
# Get the message you want to repeat
message = input("Mensaje prueba ")
# Get the number of times you want to repeat the message
num_repeats = 5
# Repeat the message the specified number of times
for i in range(num_repeats):
    pyautogui.typewrite(message)
    pyautogui.press("enter")
    time.sleep(1)
#install this:
    pip install pyautogui
