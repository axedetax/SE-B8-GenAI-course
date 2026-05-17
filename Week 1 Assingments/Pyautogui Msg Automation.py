from playwright.sync_api import sync_playwright
from datetime import datetime
import urllib.parse
import time

# =========================
# CHECK DATE
# =========================

today = datetime.now()

# Send only on 2nd day of month
if today.day != 2:
    print("Today is not the 2nd. No message sent.")
    exit()

# =========================
# CLIENT DETAILS
# =========================

phone_number = "919159533166"

message = """
Hi, Can you please share the Purchase and sales data to file GST return
"""

encoded_message = urllib.parse.quote(message)

whatsapp_url = f"https://web.whatsapp.com/send?phone={phone_number}&text={encoded_message}"

# =========================
# PLAYWRIGHT AUTOMATION
# =========================

with sync_playwright() as p:

    browser = p.chromium.launch(
        headless=False
    )

    context = browser.new_context()

    page = context.new_page()

    print("Opening WhatsApp Web...")

    page.goto(whatsapp_url)

    print("Scan QR code if required...")

    # Wait for WhatsApp to load
    page.wait_for_timeout(150000000)

    try:
        # Wait for send button
        send_button = page.locator('span[data-icon="send"]')

        send_button.wait_for(timeout=30000)

        # Click send
        send_button.click()

        print("GST reminder message sent successfully!")

    except Exception as e:
        print("Error occurred:", e)

    time.sleep(5)

    browser.close()