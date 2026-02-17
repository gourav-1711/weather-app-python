from kivy.lang import Builder
from kivymd.uix.floatlayout import MDFloatLayout

layout = """
#:import get_color_from_hex kivy.utils.get_color_from_hex
#:import Gradient kivy_gradient.Gradient
#:import RoundedRectangle kivy.graphics.RoundedRectangle
<Background>:
    canvas.before:
        # White/light gray full background
        Color:
            rgba: get_color_from_hex("F6F7F8") + [1]
        Rectangle:
            pos: self.pos
            size: self.size

        # Blue gradient top half with rounded bottom corners
        Color:
            rgba: (1, 1, 1, 1)
        RoundedRectangle:
            pos: (0, self.height * 0.50)
            size: (self.width, self.height * 0.55)
            radius: [0, 0, 40, 40]
            texture: 
                Gradient.vertical(
                get_color_from_hex("7EBCF7"), 
                get_color_from_hex("5DA9F3"),
                get_color_from_hex("2B8CEE")
                )
    

"""


class Background(MDFloatLayout):
    Builder.load_string(layout)
