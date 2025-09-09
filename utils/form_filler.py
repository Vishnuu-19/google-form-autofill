# utils/form_filler.py
import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

CSV_FILE = "data/users.csv"

def load_users():
    with open(CSV_FILE, mode="r", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))

def find_user_by_roll(roll_no):
    users = load_users()
    for user in users:
        if user["RollNo"].strip() == roll_no:
            return user
    return None

def fill_google_form(form_url, user_data):
    options = Options()
    options.binary_location = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

    # 👇 use your existing Brave profile
    options.add_argument(r"user-data-dir=C:\Users\vishn\AppData\Local\BraveSoftware\Brave-Browser\User Data")
    options.add_argument("profile-directory=Default")  # or "Profile 1" if you use another profile

    service = Service(r"C:\Users\vishn\OneDrive\Documents\google-form-autofill\drivers\chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=options)

    driver.get(form_url)
    time.sleep(3)

    # Find input & textarea fields in the form
    inputs = driver.find_elements(
        By.XPATH, '//div[@role="listitem"]//input | //div[@role="listitem"]//textarea'
    )
    print(f"🔎 Found {len(inputs)} fields in the form")

    if len(inputs) >= 7:
        inputs[0].send_keys(user_data["Name"])
        inputs[1].send_keys(user_data["Email"])
        inputs[2].send_keys(user_data["Phone"])
        inputs[3].send_keys(user_data["RollNo"])
        inputs[4].send_keys(user_data["CGPA_10"])
        inputs[5].send_keys(user_data["Inter_Percentage"])
        inputs[6].send_keys(user_data["BTech_CGPA"])
        print("✅ Form fields filled successfully.")
    else:
        print("⚠️ Not all fields found! Check XPath mapping.")

    input("👉 Press Enter to close browser after review...")
    driver.quit()
