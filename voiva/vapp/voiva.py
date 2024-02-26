import os
import sys
modelPath = os.path.abspath("../voiva")
sys.path.append(modelPath)
from kivy.app import App
from wm import WindowManager

class VoivaApp(App):
    def build(self):
        w_manager = WindowManager()
        return w_manager

if __name__ == '__main__':
    VoivaApp().run()
