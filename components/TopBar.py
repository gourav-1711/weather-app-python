from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.dialog import (
    MDDialog,
    MDDialogHeadlineText,
    MDDialogSupportingText,
    MDDialogButtonContainer,
)
from kivymd.uix.button import MDButton, MDButtonText
from kivy.uix.widget import Widget
from kivymd.app import MDApp
from components.kv.Header import layout
from kivymd.app import MDApp



Builder.load_string(layout)

class TopBar(MDBoxLayout ):
    dialog = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.main_screen = kwargs.get("main_screen")

    def on_search(self):
        search_text : str = self.ids.search_field.text
        
        if not search_text:
            self.show_dialog()
            return
        else:
           app = MDApp.get_running_app()
           app.search_weather(search_text)

    def show_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                MDDialogHeadlineText(
                    text="Empty Search",
                    halign="left",
                ),
                MDDialogSupportingText(
                    text="Please enter a city name before searching.",
                    halign="left",
                    padding=[0, "8dp", 0, "8dp"]
                ),
                MDDialogButtonContainer(
                    Widget(),
                    MDButton(
                        MDButtonText(text="OK"),
                        style="filled",
                        on_release=lambda _: self.dialog.dismiss(),
                    ),                    
                ),
            )
            self.dialog.open()
        else:
            self.dialog.open()
    