from kivy.lang import Builder
from kivymd.app import MDApp

class VoiVaApp(MDApp):
    def build(self):
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.theme_style = "Light"
        # self.theme_cls.bg_light = [1, 1, 1, 1]  # Define bg_light color
        # self.theme_cls.bg_dark = [0, 0, 0, 1]   # Define bg_dark color
        return Builder.load_file("voiva.kv")
    
    def on_start(self):
        self.fps_monitor_start()

    def switch_theme_style(self):
        if self.theme_cls.theme_style == "Light":
            self.theme_cls.theme_style = "Dark"
        else:
            self.theme_cls.theme_style = "Light"

VoiVaApp().run()
