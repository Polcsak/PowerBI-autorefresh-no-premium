import pyautogui
import time
import os

# Path to the Power BI file (.pbix)
pbix_path = r"path/to/your/PowerBI_file.pbix"

# Open the Power BI file
print("Opening the Power BI file...")
os.startfile(pbix_path)

# Wait for the Power BI application to load
time.sleep(15)

# Replace the following placeholder coordinates with the actual values obtained from Screenshot_Locator.py
refresh_button_coords = (0, 0)         # Coordinates for the refresh button
save_button_coords = (0, 0)            # Coordinates for the save button
publish_button_coords = (0, 0)         # Coordinates for the Publish button
workspace_coords = (0, 0)              # Coordinates for selecting the workspace
confirm_publish_coords = (0, 0)        # Coordinates for confirming publishing
confirm_replace_coords = (0, 0)        # Coordinates for confirming Replace

# Move to the refresh button and click
pyautogui.moveTo(refresh_button_coords[0], refresh_button_coords[1], duration=0.5)
pyautogui.click()
print("Clicked the refresh button.")

time.sleep(15)

# Move to the save button and click
pyautogui.moveTo(save_button_coords[0], save_button_coords[1], duration=0.5)
pyautogui.click()
print("Clicked the save button.")

time.sleep(3)

# Move to the Publish button and click
pyautogui.moveTo(publish_button_coords[0], publish_button_coords[1], duration=0.5)
pyautogui.click()
print("Clicked the Publish button.")

# Wait for the Publish dialog to load
time.sleep(5)

# Move to the workspace and click
pyautogui.moveTo(workspace_coords[0], workspace_coords[1], duration=0.5)
pyautogui.click()
print("Clicked the workspace.")

time.sleep(3)

# Move to the "Select" or "Confirm" button for publishing and click
pyautogui.moveTo(confirm_publish_coords[0], confirm_publish_coords[1], duration=0.5)
pyautogui.click()
print("Confirmed publishing.")

time.sleep(3)

# Move to the "Select" or "Confirm" button for Replace and click
pyautogui.moveTo(confirm_replace_coords[0], confirm_replace_coords[1], duration=0.5)
pyautogui.click()
print("Confirmed Replace.")
