import pyautogui
import time

# Image paths
file_path = 'slide_images/file.png'
make_copy_path = 'slide_images/make_a_copy.png'
entire_presentation_path = 'slide_images/entire_presentation.png'
make_copy_button_path = 'slide_images/make_a_copy_button.png'

while True:
    try:
        # Locate and click on the file image
        file_location = pyautogui.locateOnScreen(file_path)
        if file_location is not None:
            file_center = pyautogui.center(file_location)
            pyautogui.click(file_center)
            pyautogui.moveTo(500, 1000)
            time.sleep(2)
            pyautogui.click()
            continue

        # Locate and click on the make a copy image
        make_copy_location = pyautogui.locateOnScreen(make_copy_path)
        if make_copy_location is not None:
            make_copy_center = pyautogui.center(make_copy_location)
            pyautogui.click(make_copy_center)
            pyautogui.moveTo(500, 1000)
            pyautogui.click()
            time.sleep(2)
            continue

        # Locate and click on the entire presentation image
        entire_presentation_location = pyautogui.locateOnScreen(entire_presentation_path)
        if entire_presentation_location is not None:
            entire_presentation_center = pyautogui.center(entire_presentation_location)
            pyautogui.click(entire_presentation_center)
            pyautogui.moveTo(500, 1000)
            pyautogui.click()
            time.sleep(2)
            continue

        # Locate and click on the make a copy button image
        make_copy_button_location = pyautogui.locateOnScreen(make_copy_button_path)
        if make_copy_button_location is not None:
            make_copy_button_center = pyautogui.center(make_copy_button_location)
            pyautogui.click(make_copy_button_center)
            pyautogui.moveTo(500, 1000)
            pyautogui.click()
            time.sleep(2)
            continue
        pyautogui.hotkey('ctrl', 'tab')
    except pyautogui.ImageNotFoundException:
        print("notfound")
        pass
