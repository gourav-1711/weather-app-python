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
from kivymd.uix.progressindicator import MDCircularProgressIndicator
from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout



layout = """
<TopBar>:
    orientation: "horizontal"
    spacing: "10dp" 
    padding: "10dp"
    adaptive_height: True
    pos_hint: {"top": 0.98}
    MDTextField:
        id: search_field
        text: "jodhpur"
        mode: "outlined"
        hint_text: "Search"
        size_hint: (0.5, None)
        height: "40dp"
        pos_hint: {"center_x": 0.5 , "center_y": 0.5}
        # multiline: False             
        on_text_validate: root.on_search()
        MDTextFieldHintText:
            text: "City Name"

        MDTextFieldHelperText:
            text: "Search For Your Location or City"
            mode: "on_focus"

        MDTextFieldTrailingIcon:
            icon: "magnify"

        MDTextFieldMaxLengthText:
            max_text_length: 15

    MDButton:
        style: "outlined"
        radius: [5, 5, 5, 5]
        pos_hint: {"center_x": .5, "center_y": .5}
        on_release: root.on_search()
        MDButtonText:
            text: "Search"
"""
Builder.load_string(layout)

class TopBar(MDBoxLayout ):
    dialog = None
    spinner = None    
    overlay = None
    def on_search(self):
        search_text = self.ids.search_field.text

        if not search_text:
            self.show_dialog()
            return
        else:
            self.ids.search_field.text = ""
            self.show_loading()

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
    
    def show_loading(self):
        app = MDApp.get_running_app()
        if not self.overlay:
            self.overlay = MDFloatLayout(
                md_bg_color=[0, 0, 0, 0.5], 
            )
        if not self.spinner:
            self.spinner = MDCircularProgressIndicator(
                size_hint=(None, None),
                size=("30dp", "30dp"),
                pos_hint={"center_x": .5, "center_y": .5},
                color=[1, 1, 1, 1],
                
            )
        if self.overlay not in app.root.children:
            app.root.add_widget(self.overlay)
        if self.spinner not in app.root.children:
            app.root.add_widget(self.spinner)