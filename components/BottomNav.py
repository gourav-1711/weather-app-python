from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty, BooleanProperty, NumericProperty

# Bottom navigation bar KV layout
nav_layout = """
#:import get_color_from_hex kivy.utils.get_color_from_hex

<BottomNav>:
    orientation: "horizontal"
    size_hint_y: None
    height: "60dp"
    md_bg_color: 1, 1, 1, 0.95
    padding: ["20dp", "8dp", "20dp", "8dp"]
    pos_hint: {"bottom": 1}
    canvas.before:
        Color:
            rgba: get_color_from_hex("E5E7EB") + [1]
        Line:
            points: [self.x, self.top, self.right, self.top]
            width: 0.5

    NavItem:
        icon_name: "home"
        label_text: "Weather"
        is_active: True

    NavItem:
        icon_name: "compass-outline"
        label_text: "Radar"
        is_active: False

    NavItem:
        icon_name: "format-list-bulleted"
        label_text: "Cities"
        is_active: False

    NavItem:
        icon_name: "cog-outline"
        label_text: "Settings"
        is_active: False


<NavItem>:
    orientation: "vertical"
    spacing: "2dp"
    size_hint_x: 1
    
    MDIcon:
        icon: root.icon_name
        halign: "center"
        theme_text_color: "Custom"
        text_color: get_color_from_hex("2b8cee") if root.is_active else get_color_from_hex("9CA3AF")
        font_size: "22sp"
        adaptive_height: True

    MDLabel:
        text: root.label_text
        halign: "center"
        font_size: "10sp"
        bold: root.is_active
        theme_text_color: "Custom"
        text_color: get_color_from_hex("2b8cee") if root.is_active else get_color_from_hex("9CA3AF")
        adaptive_height: True
"""

Builder.load_string(nav_layout)


class NavItem(MDBoxLayout):
    icon_name = StringProperty("home")
    label_text = StringProperty("Home")
    is_active = BooleanProperty(False)


class BottomNav(MDBoxLayout):
    pass
