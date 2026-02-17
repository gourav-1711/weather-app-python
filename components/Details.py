default_weather = {
    "coord": {"lon": 77.2167, "lat": 28.6667},
    "weather": [{"id": 721, "main": "Haze", "description": "haze", "icon": "50n"}],
    "base": "stations",
    "main": {
        "temp": 18.05,
        "feels_like": 17.79,
        "temp_min": 18.05,
        "temp_max": 18.05,
        "pressure": 1014,
        "humidity": 72,
        "sea_level": 1014,
        "grnd_level": 989,
    },
    "visibility": 4000,
    "wind": {"speed": 0, "deg": 0},
    "clouds": {"all": 0},
    "dt": 1771169857,
    "sys": {
        "type": 1,
        "id": 9165,
        "country": "IN",
        "sunrise": 1771118999,
        "sunset": 1771159250,
    },
    "timezone": 19800,
    "id": 1273294,
    "name": "Delhi",
    "cod": 200,
    "hourly": [],
    "daily": [],
}

from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from components.kv.Section import Section
from kivy.properties import DictProperty, StringProperty, BooleanProperty
from components.utility import get_weather_icon, get_wind_direction

Builder.load_string(Section)


class HourlyItem(MDBoxLayout):
    time_text = StringProperty("Now")
    icon_name = StringProperty("weather-sunny")
    temp_text = StringProperty("0°")
    is_now = BooleanProperty(False)


class DailyForecastRow(MDBoxLayout):
    day_text = StringProperty("Today")
    icon_name = StringProperty("weather-sunny")
    temp_min = StringProperty("0")
    temp_max = StringProperty("0")
    is_today = BooleanProperty(False)
    is_sunny = BooleanProperty(False)


class Details(MDBoxLayout):
    weather = DictProperty(default_weather)
    weather_icon = StringProperty("weather-sunny")
    wind_direction_text = StringProperty("From the N")

    def update_data(self, data):
        self.weather = data

        # Update main weather icon
        icon_code = data["weather"][0].get("icon", "01d")
        self.weather_icon = get_weather_icon(icon_code)

        # Update wind direction
        wind_deg = data.get("wind", {}).get("deg", 0)
        self.wind_direction_text = f"From the {get_wind_direction(wind_deg)}"

        # Update hourly forecast
        self._update_hourly(data.get("hourly", []))

        # Update daily forecast
        self._update_daily(data.get("daily", []))

    def _update_hourly(self, hourly_data):
        container = self.ids.get("hourly_container")
        if not container:
            return
        container.clear_widgets()
        for item in hourly_data:
            icon = get_weather_icon(item["icon"])
            widget = HourlyItem(
                time_text=item["time"],
                icon_name=icon,
                temp_text=f"{item['temp']}°",
                is_now=(item["time"] == "Now"),
            )
            container.add_widget(widget)

    def _update_daily(self, daily_data):
        container = self.ids.get("daily_container")
        if not container:
            return
        container.clear_widgets()
        for item in daily_data:
            icon = get_weather_icon(item["icon"])
            is_sunny = icon in ("weather-sunny", "weather-partly-cloudy")
            widget = DailyForecastRow(
                day_text=item["day"],
                icon_name=icon,
                temp_min=str(item["temp_min"]),
                temp_max=str(item["temp_max"]),
                is_today=(item["day"] == "Today"),
                is_sunny=is_sunny,
            )
            container.add_widget(widget)
