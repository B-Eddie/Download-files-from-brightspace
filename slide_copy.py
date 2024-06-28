import pyautogui
import time

# Prompt the user for the coordinates
filex = int(73)
filey = int(165)

copyx = int(filex)
copyy = int(filey + 102)

x3 = int(copyx + 427)
y3 = int(copyy)

x4 = int(filex + 1304)
y4 = int(filey + 754)
pyautogui.moveTo(1200, 830)
pyautogui.click()

while True:
    time.sleep(1)
    pyautogui.moveTo(filex, filey)
    pyautogui.click()
    
    pyautogui.moveTo(copyx, copyy)
    pyautogui.click()
    
    pyautogui.moveTo(x3, y3)
    pyautogui.click()
    
    pyautogui.moveTo(x4, y4)
    pyautogui.click()
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'tab')
