layout = """
#:import get_color_from_hex kivy.utils.get_color_from_hex
#:import dp kivy.metrics.dp
#:import FrostedGlass kivy_garden.frostedglass

<TopBar>:
    size_hint_y: None
    height: "56dp"
    pos_hint: {"center_x": 0.5, "top": 0.98}
    size_hint_x: 0.95
    md_bg_color: 0, 0, 0, 0
    orientation: "horizontal"

    MDRelativeLayout:
        size_hint: (1, 1)

        FrostedGlass:
            id: frost_bar
            size_hint: (1, 1)
            background: app.bg_widget
            blur_size: 18
            saturation: 1.4
            luminosity: 1.15
            overlay_color: get_color_from_hex("#FFFFFF22")
            noise_opacity: 0.06
            border_radius: dp(28), dp(28), dp(28), dp(28)

        MDBoxLayout:
            size_hint: (1, 1)
            orientation: "horizontal"
            spacing: "8dp"
            padding: ["8dp", "6dp", "6dp", "6dp"]

            canvas.before:
                Color:
                    rgba: 1, 1, 1, 0.4
                Line:
                    rounded_rectangle: (self.x, self.y, self.width, self.height, dp(28))
                    width: 1.2

            MDRelativeLayout:
                size_hint: (1, 1)

                canvas.before:
                    Color:
                        rgba: 1, 1, 1, 0
                    RoundedRectangle:
                        pos: self.pos
                        size: self.size
                        radius: [dp(22), dp(22), dp(22), dp(22)]
                    Color:
                        rgba: 1, 1, 1, 0
                    Line:
                        rounded_rectangle: (self.x, self.y, self.width, self.height, dp(22))
                        width: 1.0

                MDBoxLayout:
                    orientation: "horizontal"
                    size_hint: (1, 1)
                    padding: ["14dp", 0, "8dp", 0]
                    spacing: "8dp"

                    MDIcon:
                        icon: "map-search-outline"
                        theme_text_color: "Custom"
                        text_color: get_color_from_hex("#ffffff")
                        font_size: "19sp"
                        size_hint: (None, 1)
                        width: "22dp"

                    TextInput:
                        id: search_field
                        hint_text: "Search city..."
                        hint_text_color: 1, 1, 1, 1
                        foreground_color: 0.05, 0.05, 0.15, 1
                        background_color: 0, 0, 0, 0
                        cursor_color: get_color_from_hex("#1A6DC4")
                        font_size: "16sp"
                        multiline: False
                        size_hint: (1, None)
                        height: "44dp"
                        padding: ["2dp", "12dp", "8dp", "12dp"]
                        pos_hint: {"center_y": 0.5}
                        on_text_validate: root.on_search()

            MDIconButton:
                icon: "magnify"
                size_hint: (None, None)
                size: "44dp", "44dp"
                pos_hint: {"center_y": 0.5}
                theme_icon_color: "Custom"
                icon_color: 1, 1, 1, 1
                on_release: root.on_search()

                canvas.before:
                    Color:
                        rgba: get_color_from_hex("#5BABF5") + [1]
                    RoundedRectangle:
                        pos: self.pos
                        size: self.size
                        radius: [dp(22), dp(22), dp(22), dp(22)]
                    Color:
                        rgba: get_color_from_hex("#1A6DC4") + [1]
                    RoundedRectangle:
                        pos: self.x, self.y
                        size: self.width, self.height * 0.55
                        radius: [0, 0, dp(22), dp(22)]
                    Color:
                        rgba: 1, 1, 1, 0.2
                    RoundedRectangle:
                        pos: self.x, self.y + self.height * 0.52
                        size: self.width, self.height * 0.48
                        radius: [dp(22), dp(22), 0, 0]
"""