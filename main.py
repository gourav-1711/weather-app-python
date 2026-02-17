from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.snackbar import (
    MDSnackbar,
    MDSnackbarText,
    MDSnackbarButtonContainer,
    MDSnackbarActionButton,
    MDSnackbarActionButtonText,
    MDSnackbarCloseButton,
)
from kivy.metrics import dp
from kivy.properties import ObjectProperty
from kivy.clock import Clock

from components.TopBar import TopBar
from components.Details import Details
from components.Loading import overlayLoading
from components.utility import get_weather
from components.Background import Background

from kivy.core.window import Window


class WeatherApp(MDApp):
    bg_widget = ObjectProperty(None, allownone=True)

    def build(self):
        self.theme_cls.primary_palette = "Blue"
        Window.size = (390, 780)
        self.screen = MDScreen(md_bg_color=[0.965, 0.969, 0.973, 1])

        # Background MUST be created and assigned before TopBar is added
        self.bg = Background()
        self.bg_widget = self.bg  # FrostedGlass references app.bg_widget

        self.top_bar = TopBar()
        self.details_section = Details()
        self.loading_spinner = overlayLoading()

        self.snack_text = MDSnackbarText(text="Initial Error")
        self.snack_retry_btn = MDSnackbarActionButton(
            MDSnackbarActionButtonText(text="Retry"),
            on_release=lambda x: self.retry_last_search(),
        )
        self.snackbar = MDSnackbar(
            self.snack_text,
            MDSnackbarButtonContainer(
                self.snack_retry_btn,
                MDSnackbarCloseButton(
                    icon="close", on_release=lambda x: self.snackbar.dismiss()
                ),
            ),
            y=dp(24),
            pos_hint={"center_x": 0.5, "top": 1},
            size_hint_x=0.8,
            orientation="horizontal",
        )

        # Order matters: background first, then content, then top bar on top
        self.screen.add_widget(self.bg)
        self.screen.add_widget(self.details_section)
        self.screen.add_widget(self.top_bar)

        self.last_city = ""
        return self.screen

    def on_start(self):
        # Delay first search one frame so layout is fully built
        Clock.schedule_once(lambda dt: self.search_weather("Delhi"), 0)

    def search_weather(self, city_name):
        if city_name == self.last_city:
            return
        self.last_city = city_name
        self.screen.add_widget(self.loading_spinner)
        get_weather(city_name, self.on_weather_result)

    def retry_last_search(self):
        self.snackbar.dismiss()
        self.last_city = ""
        self.search_weather(self.last_city)

    def on_weather_result(self, result):
        self.screen.remove_widget(self.loading_spinner)
        if result["status"]:
            self.details_section.update_data(result["data"])
            city = result["data"].get("name", "")
            if city:
                self.top_bar.city_name = f"⌂ {city}"
        else:
            self.show_error(result["error"])

    def show_error(self, message):
        self.snack_text.text = message
        if not self.snackbar.parent:
            self.snackbar.open()


if __name__ == "__main__":
    WeatherApp().run()