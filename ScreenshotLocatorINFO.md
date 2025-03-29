# Image Position Finder Script

This script locates the on-screen position of a specific image (for example, a "Publish" button in Power BI) using PyAutoGUI. It also saves a debug screenshot of your current screen.

## Setup

1. **Save Your Image:**
   - Capture the screenshot (or image snippet) of the element you want to locate.
   - Save the image as a PNG file (e.g., `replace.png`).
   - Place the image in your chosen folder (for example:  
     `C:\Users\jakub\SynologyDrive\osobna_zlozka\Projects\Overviews\Finance_Overview\Refresh_powerBI\`).
   - Update the `image_path` variable in the script with the correct file path to your image.

2. **Debug Screenshot:**
   - The script saves a screenshot of your entire screen to the desktop as `debug_screen.png`. This is useful for debugging and ensuring your target window is correctly captured.

## How It Works

1. **Image Verification:**
   - The script checks if the specified PNG file exists. If it doesn’t, it prints an error message.

2. **Waiting for the Target Window:**
   - It waits for 2 seconds to allow you time to focus on the relevant window (e.g., Power BI).

3. **Locating the Image:**
   - Using `pyautogui.locateOnScreen` with a confidence of 0.8, the script searches for the image on the screen.
   - If the image is found, it calculates the center of the image's bounding box.
   - It prints the coordinates and moves the mouse pointer to the center of the image.
   - If the image is not found, it prints an error message with a suggestion to try a different image or adjust the confidence level.

4. **Error Handling:**
   - If PyAutoGUI fails to locate the image (throwing an `ImageNotFoundException`), the script prints an error message advising you to check the image quality or lower the confidence threshold.

## Running the Script

- Open your terminal or command prompt.
- Run the script using Python:
  ```bash
  python your_script_name.py
