import pyautogui
import webbrowser
import time

# WhatsApp number in international format (no + or spaces)
phone_number = "+919712534629"  # Replace with your target number

# Message and number of times to send
message = "Hello from PyAutoGUI!"
num_messages = 20

# 1. Open WhatsApp chat in browser
webbrowser.open(f"https://wa.me/{phone_number}")
print("Opening WhatsApp Web...")
time.sleep(10)  # Wait for WhatsApp Web to load

# 2. Click on the 'Continue to Chat' and 'Use WhatsApp Web' manually (if needed)
# Or automate it if needed with pyautogui.click()

# 3. After chat loads, send messages
print("Sending messages...")
for i in range(num_messages):
    pyautogui.typewrite(f"{message} #{i+1}")
    pyautogui.press("enter")
    time.sleep(0.3)
