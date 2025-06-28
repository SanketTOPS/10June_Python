"""import pywhatkit

pywhatkit.sendwhatmsg_instantly("+919724799469","Hello Students!This is Testing")"""


import pywhatkit
import time

phone_number = "+919724799469"  # Replace with the target number
message = "This is a test message."  # Message to send

# Loop to send 10 messages
for i in range(10):
    try:
        pywhatkit.sendwhatmsg_instantly(
            phone_no=phone_number,
            message=f"{message} #{i+1}",
            wait_time=10,   # Seconds to wait after opening WhatsApp Web before sending
            tab_close=True  # Automatically close the tab
        )
        print(f"Sent message {i+1}")
        time.sleep(3)  # Short delay to avoid triggering anti-spam
    except Exception as e:
        print(f"Failed to send message {i+1}: {e}")
        time.sleep(5)  # Wait a bit before retrying if there's an error
