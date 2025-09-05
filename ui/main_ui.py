import flet as ft

def run_app():
    def main(page: ft.Page):
        page.title = "Google Form Autofill"

        url_input = ft.TextField(label="Enter google from link",width = 400)

        def on_submit(e):
            page.add(ft.Text(f"processing:{url_input.value}"))

        submit_btn = ft.ElevatedButton("Submit",on_click=on_submit)
        page.add(url_input,submit_btn)

    ft.app(target=main)