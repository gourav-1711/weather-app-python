from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from components.TopBar import TopBar


class WeatherApp(MDApp):
    def get_weather():
        pass
    
    def build(self):
        screen = MDScreen(md_bg_color="white")
        top_bar = TopBar()

        screen.add_widget(top_bar)
        
        return screen


if __name__ == "__main__":
    WeatherApp().run()