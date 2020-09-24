import pyautogui
import time

pyautogui.FAILSAFE = False

time.sleep(5)
pyautogui.press('j')
# this loop will run for 3 times.
for i in range(0, 3):
    time.sleep(3)
    pyautogui.press('c')
    time.sleep(4)
    pyautogui.typewrite('This is a test message')
    time.sleep(2)
    pyautogui.press('enter')

    # this loop will press tab 5 times to go to the next post
    j = 5
    while j > 0 and i < 2:
        print(i)
        time.sleep(1)
        pyautogui.press('tab')
        j = j - 1
