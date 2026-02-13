from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDButton, MDButtonIcon, MDButtonText
class Layout(MDBoxLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        label = MDLabel(
                text="Hello World",
                halign="center",
                pos_hint={"center_x": 0.5, "center_y": 0.5},
                text_color="red"
            )
        self.add_widget(label)
        button = MDButton(MDButtonText(
                        text="Elevated",
                    ))
      
        self.add_widget(button)

class WeatherApp(MDApp):
    def build(self):
        screen = MDScreen(md_bg_color="white")
        
        layout = Layout()
        screen.add_widget(layout)
        
        return screen

if __name__ == "__main__":
    WeatherApp().run()