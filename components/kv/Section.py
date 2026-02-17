Section = """
#:import get_color_from_hex kivy.utils.get_color_from_hex

<Details>:
    orientation: "vertical"

    ScrollView:
        do_scroll_x: False
        bar_width: "0dp"

        MDBoxLayout:
            orientation: "vertical"
            size_hint_y: None
            height: self.minimum_height
            spacing: "8dp"
            padding: ["0dp", "0dp", "0dp", "60dp"]

            # ===== HERO SECTION =====
            Widget:
                size_hint_y: None
                height: "56dp"

            # City name
            MDBoxLayout:
                size_hint_y: None
                height: "24dp"
                spacing: "4dp"
                pos_hint: {"center_x": 0.5}
                size_hint_x: None
                width: self.minimum_width

                MDIcon:
                    icon: "near-me"
                    theme_text_color: "Custom"
                    text_color: 1, 1, 1, 0.9
                    font_size: "16sp"
                    pos_hint: {"center_y": 0.5}

                MDLabel:
                    text: root.weather["name"]
                    halign: "center"
                    font_size: "18sp"
                    bold: True
                    theme_text_color: "Custom"
                    text_color: 1, 1, 1, 1
                    adaptive_size: True

            # Weather Icon
            MDIcon:
                icon: root.weather_icon
                halign: "center"
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                font_size: "180sp"
                adateptive_size: True
                size_hint: None, None
                size: self.texture_size
                pos_hint: {"center_x": 0.5}

            # Temperature
            MDBoxLayout:
                size_hint_y: None
                height: "50dp"
                size_hint_x: None
                width: self.minimum_width
                pos_hint: {"center_x": .5}
                orientation: "horizontal"
                MDLabel:
                    text: f"{int(root.weather['main']['temp'])}"
                    font_size: "80sp"
                    theme_text_color: "Custom"
                    text_color: 1, 1, 1, 1
                    adaptive_size: True

                MDLabel:
                    text: "°C"
                    font_size: "26sp"
                    theme_text_color: "Custom"
                    text_color: 1, 1, 1, 1
                    adaptive_size: True
                    

            # Description
            MDLabel:
                text: root.weather['weather'][0]['description'].title()
                halign: "center"
                font_size: "18sp"
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 0.9
                size_hint_y: None
                height: "24dp"

            # H/L Pill
            MDBoxLayout:
                size_hint: None, None
                size: "150dp", "32dp"
                pos_hint: {"center_x": .5}
                radius: [16, 16, 16, 16]
                canvas.before:
                    Color:
                        rgba: 1, 1, 1, 0.2
                    RoundedRectangle:
                        pos: self.pos
                        size: self.size
                        radius: self.radius

                MDLabel:
                    text: f"H: {int(root.weather['main']['temp_max'])}°  L: {int(root.weather['main']['temp_min'])}°"
                    halign: "center"
                    valign: "center"
                    font_size: "13sp"
                    theme_text_color: "Custom"
                    text_color: 1, 1, 1, 1

            # ===== CARDS =====
            Widget:
                size_hint_y: None
                height: "10dp"

            # --- HOURLY FORECAST ---
            MDBoxLayout:
                orientation: "vertical"
                size_hint: 0.92, None
                height: self.minimum_height
                pos_hint: {"center_x": 0.5}
                padding: ["16dp", "14dp", "16dp", "10dp"]
                radius: [16, 16, 16, 16]
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 0.06
                    RoundedRectangle:
                        pos: self.x + 1, self.y - 3
                        size: self.width - 2, self.height
                        radius: self.radius
                    Color:
                        rgba: 1, 1, 1, 1
                    RoundedRectangle:
                        pos: self.pos
                        size: self.size
                        radius: self.radius

                MDBoxLayout:
                    size_hint_y: None
                    height: "28dp"
                    padding: ["0dp", "0dp", "0dp", "8dp"]

                    MDLabel:
                        text: "HOURLY FORECAST"
                        font_size: "11sp"
                        bold: True
                        theme_text_color: "Custom"
                        text_color: get_color_from_hex("9CA3AF")
                        adaptive_height: True

                    MDIcon:
                        icon: "clock-outline"
                        theme_text_color: "Custom"
                        text_color: get_color_from_hex("D1D5DB")

                ScrollView:
                    do_scroll_y: False
                    bar_width: "0dp"
                    size_hint_y: None
                    height: "90dp"

                    MDBoxLayout:
                        id: hourly_container
                        orientation: "horizontal"
                        spacing: "20dp"
                        size_hint_x: None
                        width: self.minimum_width

            # --- HUMIDITY & WIND ---
            MDGridLayout:
                cols: 2
                spacing: "10dp"
                size_hint: 0.92, None
                height: "120dp"
                pos_hint: {"center_x": 0.5}

                # Humidity
                MDBoxLayout:
                    orientation: "vertical"
                    padding: ["12dp", "10dp", "12dp", "8dp"]
                    spacing: "2dp"
                    radius: [16, 16, 16, 16]
                    canvas.before:
                        Color:
                            rgba: 0, 0, 0, 0.06
                        RoundedRectangle:
                            pos: self.x + 1, self.y - 3
                            size: self.width - 2, self.height
                            radius: self.radius
                        Color:
                            rgba: 1, 1, 1, 1
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: self.radius

                    MDBoxLayout:
                        adaptive_height: True
                        spacing: "6dp"

                        MDIcon:
                            icon: "water-outline"
                            theme_text_color: "Custom"
                            text_color: get_color_from_hex("9CA3AF")
                            font_size: "14sp"

                        MDLabel:
                            text: "HUMIDITY"
                            font_size: "9sp"
                            bold: True
                            theme_text_color: "Custom"
                            text_color: get_color_from_hex("9CA3AF")
                            adaptive_height: True

                    MDLabel:
                        text: f"{root.weather['main']['humidity']}%"
                        font_size: "26sp"
                        bold: True
                        theme_text_color: "Custom"
                        text_color: get_color_from_hex("1E293B")
                        adaptive_height: True

                    MDLabel:
                        text: "Normal dew point"
                        font_size: "11sp"
                        theme_text_color: "Custom"
                        text_color: get_color_from_hex("9CA3AF")
                        adaptive_height: True

                # Wind
                MDBoxLayout:
                    orientation: "vertical"
                    padding: ["12dp", "10dp", "12dp", "8dp"]
                    spacing: "2dp"
                    radius: [16, 16, 16, 16]
                    canvas.before:
                        Color:
                            rgba: 0, 0, 0, 0.06
                        RoundedRectangle:
                            pos: self.x + 1, self.y - 3
                            size: self.width - 2, self.height
                            radius: self.radius
                        Color:
                            rgba: 1, 1, 1, 1
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: self.radius

                    MDBoxLayout:
                        adaptive_height: True
                        spacing: "6dp"

                        MDIcon:
                            icon: "weather-windy"
                            theme_text_color: "Custom"
                            text_color: get_color_from_hex("9CA3AF")
                            font_size: "14sp"

                        MDLabel:
                            text: "WIND"
                            font_size: "9sp"
                            bold: True
                            theme_text_color: "Custom"
                            text_color: get_color_from_hex("9CA3AF")
                            adaptive_height: True

                    MDBoxLayout:
                        adaptive_height: True
                        spacing: "4dp"

                        MDLabel:
                            text: f"{int(root.weather['wind']['speed'])}"
                            font_size: "26sp"
                            bold: True
                            theme_text_color: "Custom"
                            text_color: get_color_from_hex("1E293B")
                            adaptive_size: True

                        MDLabel:
                            text: "km/h"
                            font_size: "13sp"
                            theme_text_color: "Custom"
                            text_color: get_color_from_hex("64748B")
                            adaptive_size: True
                            pos_hint: {"center_y": 0.4}

                    MDLabel:
                        text: root.wind_direction_text
                        font_size: "11sp"
                        theme_text_color: "Custom"
                        text_color: get_color_from_hex("9CA3AF")
                        adaptive_height: True

            # --- 5-DAY FORECAST ---
            MDBoxLayout:
                orientation: "vertical"
                size_hint: 0.92, None
                height: self.minimum_height
                pos_hint: {"center_x": 0.5}
                padding: ["16dp", "14dp", "16dp", "10dp"]
                radius: [16, 16, 16, 16]
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 0.06
                    RoundedRectangle:
                        pos: self.x + 1, self.y - 3
                        size: self.width - 2, self.height
                        radius: self.radius
                    Color:
                        rgba: 1, 1, 1, 1
                    RoundedRectangle:
                        pos: self.pos
                        size: self.size
                        radius: self.radius

                MDBoxLayout:
                    size_hint_y: None
                    height: "28dp"
                    padding: ["0dp", "0dp", "0dp", "10dp"]

                    MDLabel:
                        text: "5-DAY FORECAST"
                        font_size: "11sp"
                        bold: True
                        theme_text_color: "Custom"
                        text_color: get_color_from_hex("9CA3AF")
                        adaptive_height: True

                    MDIcon:
                        icon: "calendar-month-outline"
                        theme_text_color: "Custom"
                        text_color: get_color_from_hex("D1D5DB")

                MDBoxLayout:
                    id: daily_container
                    orientation: "vertical"
                    spacing: "14dp"
                    size_hint_y: None
                    height: self.minimum_height


# ===== HOURLY ITEM =====
<HourlyItem>:
    orientation: "vertical"
    spacing: "6dp"
    size_hint: None, None
    size: "50dp", "85dp"

    MDLabel:
        text: root.time_text
        halign: "center"
        font_size: "11sp"
        bold: root.is_now
        theme_text_color: "Custom"
        text_color: get_color_from_hex("6B7280")
        adaptive_height: True

    MDIcon:
        icon: root.icon_name
        halign: "center"
        theme_text_color: "Custom"
        text_color: get_color_from_hex("2b8cee")
        font_size: "24sp"
        size_hint: None, None
        size: "28dp", "28dp"
        pos_hint: {"center_x": 0.5}

    MDLabel:
        text: root.temp_text
        halign: "center"
        font_size: "14sp"
        bold: True
        theme_text_color: "Custom"
        text_color: get_color_from_hex("1E293B")
        adaptive_height: True


# ===== DAILY FORECAST ROW =====
<DailyForecastRow>:
    size_hint_y: None
    height: "40dp"
    spacing: "8dp"
    padding: [0, "4dp", 0, "4dp"]
    MDLabel:
        text: root.day_text
        font_size: "15sp"
        bold: root.is_today
        theme_text_color: "Custom"
        text_color: get_color_from_hex("1E293B") if root.is_today else get_color_from_hex("475569")
        size_hint_x: 0.25
        adaptive_height: True

    MDIcon:
        icon: root.icon_name
        halign: "center"
        theme_text_color: "Custom"
        text_color: get_color_from_hex("2b8cee") if root.is_sunny else get_color_from_hex("9CA3AF")
        font_size: "22sp"
        size_hint_x: 0.2

    Widget:
        size_hint_x: 0.1

    MDLabel:
        text: f"{root.temp_min}°"
        halign: "right"
        font_size: "14sp"
        theme_text_color: "Custom"
        text_color: get_color_from_hex("9CA3AF")
        size_hint_x: 0.15
        adaptive_height: True

    MDLabel:
        text: f"{root.temp_max}°"
        halign: "right"
        font_size: "15sp"
        bold: True
        theme_text_color: "Custom"
        text_color: get_color_from_hex("1E293B")
        size_hint_x: 0.15
        adaptive_height: True
"""
