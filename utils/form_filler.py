import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService

CSV_FILE = "data/users.csv"
EDGE_DRIVER_PATH = r"C:\WebDriver\msedgedriver.exe"  # <-- Update this path if needed

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
    # Use Microsoft Edge browser with local driver
    service = EdgeService(executable_path=EDGE_DRIVER_PATH)
    driver = webdriver.Edge(service=service)

    driver.get(form_url)

    inputs = driver.find_elements(By.XPATH, '//input[@type="text"]')

    if len(inputs) >= 4:
        inputs[0].send_keys(user_data["Name"])
        inputs[1].send_keys(user_data["Email"])
        inputs[2].send_keys(user_data["Phone"])
        inputs[3].send_keys(user_data["RollNo"])
    
    print("✅ Form filled. Review it in Edge browser...")

    time.sleep(30)

    try:
        submit_btn = driver.find_element(By.XPATH, '//span[text()="Submit"]/ancestor::button')
        submit_btn.click()
        print("🚀 Form submitted!")
    except Exception as e:
        print("⚠️ Could not find the submit button. Please submit manually.")

    time.sleep(5)
    driver.quit()
