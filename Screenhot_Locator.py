import pyautogui
import time
import os

# Path to the image of the Publish button
image_path = r"path/to/your/image.png"

# Check if the PNG image exists
if not os.path.exists(image_path):
    print(f"Image not found: {image_path}")
else:
    time.sleep(2)  # Wait for 2 seconds to ensure the target window is active

    try:
        location = pyautogui.locateOnScreen(image_path, confidence=0.8)

        if location:
            x_center = location.left + location.width / 2
            y_center = location.top + location.height / 2

            print(f"Found the Publish button at position: ({x_center}, {y_center})")
            pyautogui.moveTo(x_center, y_center, duration=0.5)
        else:
            print("Publish button not found. Try a different image or lower the confidence level.")

    except pyautogui.ImageNotFoundException:
        print("PyAutoGUI could not find the image. Check its quality or lower the confidence level.")


