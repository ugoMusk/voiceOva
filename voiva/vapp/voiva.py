import os
import sys
modelPath = os.path.abspath("../voiva")
sys.path.append(modelPath)
from kivy.app import App
# from layout import create
# from layout import home
# from layout import docs
from wm import WindowManager

class VoivaApp(App):
    def build(self):
        w_manager = WindowManager()
        # w_manager.add_widget(create.CreateWindow(name='create'))
        # w_manager.add_widget(home.HomeWindow(name='home'))
        # w_manager.add_widget(docs.DocsWindow(name='docs'))
        return w_manager

if __name__ == '__main__':
    VoivaApp().run()
