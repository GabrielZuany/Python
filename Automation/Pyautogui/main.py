import pyautogui
from time import sleep
#pyautogui.KEYBOARD_KEYS

pyautogui.PAUSE = 1 # 1 sec delay after each line.
pyautogui.alert("You computer will be controlled automatically by a Python script. Dont press anything.")


# ---- Open spotify -------

pyautogui.press('win') # to press the windows key
pyautogui.write('spotify') # to write a text message
pyautogui.press('enter') # to press the enter key
sleep(7)
#pyautogui.hotkey('win', 'd') # to press more than one key at same time


# ---- Move the mouse to elements on screen ------

pyautogui.moveTo(117, 142) # my lib Point(x=117, y=142)
pyautogui.click() # or pyautogui.click(117, 142) to move then click
sleep(2)
pyautogui.moveTo(811, 262) # play playlist Point(x=811, y=262) 
pyautogui.click()

# ------- end message ---------

pyautogui.alert("The script has been finished, you can now use your computer.")