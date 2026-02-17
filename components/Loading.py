from kivy.lang import Builder
from kivymd.uix.floatlayout import MDFloatLayout
string = """
<overlayLoading>:
    id: overlayLoading
    md_bg_color: 0, 0, 0, .5
    MDCircularProgressIndicator:
        size_hint: None, None
        size: "30dp", "30dp"
        pos_hint: {"center_x": .5, "center_y": .5}
        color: 1, 1, 1, 1
"""

class overlayLoading(MDFloatLayout):
    Builder.load_string(string)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            return True
        return super().on_touch_down(touch)
    