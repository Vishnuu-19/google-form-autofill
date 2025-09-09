# ui/main_ui.py
import flet as ft
from utils.form_filler import find_user_by_roll, fill_google_form

def run_app():
    def main(page: ft.Page):
        page.title = "Google Form Autofill"

        # Input fields
        url_input = ft.TextField(label="Enter Google Form URL", width=600)
        roll_input = ft.TextField(label="Enter Roll No", width=400)
        output = ft.Text("")

        # Event handler
        def on_submit(e):
            form_url = url_input.value.strip()
            roll_no = roll_input.value.strip()

            if not form_url.startswith("https://docs.google.com/forms/"):
                output.value = "⚠️ Invalid Google Form URL."
            else:
                user = find_user_by_roll(roll_no)
                if user:
                    output.value = "✅ Record found! Opening form..."
                    page.update()
                    fill_google_form(form_url, user)
                else:
                    output.value = f"❌ No record found for Roll No {roll_no}."
            
            page.update()

        # Button
        submit_btn = ft.ElevatedButton("Fill Google Form", on_click=on_submit)

        # Add to page
        page.add(url_input, roll_input, submit_btn, output)

    ft.app(target=main)
