from kivymd.uix.floatlayout import MDFloatLayout
from kivy.lang.builder import Builder
layout = """
#:import get_color_from_hex kivy.utils.get_color_from_hex
#:import Gradient kivy_gradient.Gradient

<Background>:
    canvas.before:
        Color:
            rgba: get_color_from_hex("F6F7F8") + [1]
        Rectangle:
            pos: self.pos
            size: self.size

        Color:
            rgba: (1, 1, 1, 1)
        RoundedRectangle:
            pos: (0, self.height * 0.50)
            size: (self.width, self.height * 0.55)
            radius: [0, 0, 40, 40]
            texture: Gradient.vertical(get_color_from_hex("7EBCF7"), get_color_from_hex("5DA9F3"), get_color_from_hex("2B8CEE"))


"""


class Background(MDFloatLayout):
    pass


Builder.load_string(layout)