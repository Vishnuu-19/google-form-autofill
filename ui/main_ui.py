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

        # Button click
        def on_submit(e):
            roll_no = roll_input.value.strip()
            form_url = url_input.value.strip()
            user = find_user_by_roll(roll_no)

            if not form_url:
                output.value = "⚠️ Please enter a Google Form URL."
            elif user:
                output.value = "✅ Record found! Opening Google Form..."
                page.update()

                fill_google_form(form_url, user)
            else:
                output.value = "❌ No record found with this Roll No."
            
            page.update()

        submit_btn = ft.ElevatedButton("Fill Google Form", on_click=on_submit)

        # Add components to the page
        page.add(
            url_input,
            roll_input,
            submit_btn,
            output
        )

    ft.app(target=main)
