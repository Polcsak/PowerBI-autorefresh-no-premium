# Power BI Automation Script

This script automates a sequence of actions in Power BI. It opens a Power BI file, refreshes the data, saves the file, and publishes the report by simulating mouse movements and clicks. A python script which autorefresh PowerBI file to service without Premium!

## How It Works

1. **Open Power BI File:**  
   The script opens the specified Power BI (.pbix) file using its file path.

2. **Wait for Application to Load:**  
   It waits a predetermined amount of time to allow Power BI to load completely.

3. **Simulate User Actions:**  
   The script performs a series of actions by moving the mouse and clicking:
   - Click the refresh button.
   - Click the save button.
   - Click the Publish button.
   - Select the workspace.
   - Confirm publishing.
   - Confirm replacing the report.

4. **Dynamic Coordinates:**  
   The coordinate values for each button are placeholders. You need to use the `Screenshot_Locator.py` script to obtain the correct coordinates for your screen and update the script accordingly.

## Setup

1. **Install Python and PyAutoGUI:**  
   Ensure you have Python 3 installed and install PyAutoGUI with:
   ```bash
   pip install pyautogui

## Configure the Script

1. **Update the pbix_path Variable:**  
   Update the `pbix_path` variable with the path to your Power BI file.

2. **Update Coordinates:**  
   Replace the placeholder coordinates (currently set as `(0, 0)`) with the actual values provided by the `Screenshot_Locator.py` script.

## Run the Script

Open your terminal or command prompt and execute the script:

```bash
python your_script_name.py

Note:
Make sure that Power BI and any necessary dialogs are visible on your screen when running the script, as the mouse actions rely on the screen positions.
