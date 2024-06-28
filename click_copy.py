import pyautogui
import time

# Path to the image you want to locate
image_path = 'copy1.png'

# Loop for the specified number of iterations
while True:
    # Locate the image on the screen
    try:
        image_location = pyautogui.locateOnScreen(image_path)
        if image_location is not None:
            # Get the center coordinates of the image
            image_center = pyautogui.center(image_location)
            
            # Click on the image
            pyautogui.click(image_center)
            # time.sleep(0.1)
            pyautogui.hotkey('ctrl', 'tab')
            pyautogui.moveTo(500, 1000)

    except pyautogui.ImageNotFoundException:
        print("notfound")
        pass