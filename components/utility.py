from kivy.network.urlrequest import UrlRequest
import os
import dotenv
from datetime import datetime, timezone, timedelta

dotenv.load_dotenv()


def get_weather(city_name, callback):
    api_key = os.getenv("API_KEY")
    if not api_key:
        print("Error: API_KEY not found in environment variables")
        callback({"status": False, "error": "API_KEY not found"})
        return

    current_url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    forecast_url = f"https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}&units=metric"

    result_data = {"current": None, "forecast": None}

    def _check_complete():
        if result_data["current"] is not None and result_data["forecast"] is not None:
            if result_data["current"]["status"] and result_data["forecast"]["status"]:
                combined = result_data["current"]["data"]
                combined["hourly"] = _parse_hourly(
                    result_data["forecast"]["data"], combined.get("timezone", 0)
                )
                combined["daily"] = _parse_daily(
                    result_data["forecast"]["data"], combined.get("timezone", 0)
                )
                callback({"status": True, "data": combined})
            else:
                err = result_data["current"].get("error") or result_data[
                    "forecast"
                ].get("error")
                callback({"status": False, "error": err or "Unknown error"})

    def on_current_success(req, res):
        result_data["current"] = {"status": True, "data": res}
        _check_complete()

    def on_current_fail(req, res):
        result_data["current"] = {
            "status": False,
            "error": "Failed to fetch current weather",
        }
        _check_complete()

    def on_forecast_success(req, res):
        result_data["forecast"] = {"status": True, "data": res}
        _check_complete()

    def on_forecast_fail(req, res):
        result_data["forecast"] = {"status": False, "error": "Failed to fetch forecast"}
        _check_complete()

    UrlRequest(
        current_url,
        on_success=on_current_success,
        on_failure=on_current_fail,
        on_error=on_current_fail,
        ca_file=None,
    )
    UrlRequest(
        forecast_url,
        on_success=on_forecast_success,
        on_failure=on_forecast_fail,
        on_error=on_forecast_fail,
        ca_file=None,
    )


def _parse_hourly(forecast_data, tz_offset):
    """Extract next 6 hourly entries from the 3-hour forecast."""
    entries = forecast_data.get("list", [])[:6]
    hourly = []
    for entry in entries:
        dt_utc = datetime.fromtimestamp(entry["dt"], tz=timezone.utc)
        dt_local = dt_utc + timedelta(seconds=tz_offset)
        hourly.append(
            {
                "time": (
                    dt_local.strftime("%-I %p")
                    if os.name != "nt"
                    else dt_local.strftime("%#I %p")
                ),
                "temp": round(entry["main"]["temp"]),
                "icon": entry["weather"][0]["icon"],
                "condition": entry["weather"][0]["main"],
            }
        )
    if hourly:
        hourly[0]["time"] = "Now"
    return hourly


def _parse_daily(forecast_data, tz_offset):
    """Group 3-hour entries by day to get daily min/max temps."""
    entries = forecast_data.get("list", [])
    days = {}
    day_names = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    for entry in entries:
        dt_utc = datetime.fromtimestamp(entry["dt"], tz=timezone.utc)
        dt_local = dt_utc + timedelta(seconds=tz_offset)
        date_key = dt_local.strftime("%Y-%m-%d")

        if date_key not in days:
            days[date_key] = {
                "date": dt_local,
                "temps": [],
                "icon": entry["weather"][0]["icon"],
                "condition": entry["weather"][0]["main"],
            }
        days[date_key]["temps"].append(entry["main"]["temp"])

    daily = []
    today_str = (datetime.now(timezone.utc) + timedelta(seconds=tz_offset)).strftime(
        "%Y-%m-%d"
    )

    for i, (date_key, info) in enumerate(sorted(days.items())):
        if i >= 5:
            break
        if date_key == today_str:
            label = "Today"
        else:
            label = day_names[info["date"].weekday()]
        daily.append(
            {
                "day": label,
                "temp_min": round(min(info["temps"])),
                "temp_max": round(max(info["temps"])),
                "icon": info["icon"],
                "condition": info["condition"],
            }
        )
    return daily


def get_wind_direction(deg):
    """Convert wind degree to compass direction string."""
    directions = [
        "N",
        "NNE",
        "NE",
        "ENE",
        "E",
        "ESE",
        "SE",
        "SSE",
        "S",
        "SSW",
        "SW",
        "WSW",
        "W",
        "WNW",
        "NW",
        "NNW",
    ]
    idx = round(deg / 22.5) % 16
    return directions[idx]


def get_weather_icon(icon_code):
    """Map OpenWeatherMap icon code to Material Design Icon name."""
    mapping = {
        "01d": "weather-sunny",
        "01n": "weather-night",
        "02d": "weather-partly-cloudy",
        "02n": "weather-night-partly-cloudy",
        "03d": "weather-cloudy",
        "03n": "weather-cloudy",
        "04d": "cloud",
        "04n": "cloud",
        "09d": "weather-rainy",
        "09n": "weather-rainy",
        "10d": "weather-pouring",
        "10n": "weather-pouring",
        "11d": "weather-lightning",
        "11n": "weather-lightning",
        "13d": "weather-snowy",
        "13n": "weather-snowy",
        "50d": "weather-fog",
        "50n": "weather-fog",
    }
    return mapping.get(icon_code, "weather-sunny")
