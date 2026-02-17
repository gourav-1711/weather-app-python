layout = """
#:import get_color_from_hex kivy.utils.get_color_from_hex
#:import FrostedGlass kivy_garden.frostedglass

<TopBar>:
    orientation: "vertical"
    spacing: "4dp"
    padding: ["12dp", "0dp", "12dp", "4dp"]
    size_hint_y: None
    # height: "108dp"
    pos_hint: {"top": 1}

    # --- ROW 1: SEARCH BAR ---
    MDBoxLayout:
        size_hint_y: None
        height: "48dp"
        spacing: "10dp"

        # Frosted search field container
        MDRelativeLayout:
            size_hint: (0.85, 1)

            FrostedGlass:
                id: frost_search
                size_hint: (1, 1)
                background: app.bg_widget
                blur_size: 25
                saturation: 1.2
                luminosity: 1.3
                overlay_color: "#FFFFFF50"
                noise_opacity: 0.05
                border_radius: dp(24), dp(24), dp(24), dp(24)

                MDBoxLayout:
                    padding: ["16dp", "0dp", "16dp", "0dp"]
                    
                    TextInput:
                        id: search_field
                        hint_text: "Search city..."
                        hint_text_color: (1, 1, 1, 0.6)
                        foreground_color: (1, 1, 1, 1)
                        background_color: (0, 0, 0, 0)
                        cursor_color: (1, 1, 1, 1)
                        font_size: "15sp"
                        multiline: False
                        size_hint_y: None
                        height: "44dp"
                        padding: ["0dp", "12dp", "0dp", "12dp"]
                        pos_hint: {"center_y": 0.5}
                        on_text_validate: root.on_search()

        # Blue search button
        MDIconButton:
            icon: "magnify"
            style: "standard"
            user_font_size: "22sp"
            size_hint: (None, None)
            size: "48dp", "48dp"
            theme_icon_color: "Custom"
            icon_color: 1, 1, 1, 1
            pos_hint: {"center_y": 0.5}
            on_release: root.on_search()

            canvas.before:
                Color:
                    rgba: get_color_from_hex("2B8CEE") + [1]
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [dp(24), dp(24), dp(24), dp(24)]

"""
