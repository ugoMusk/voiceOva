from kivy.uix.screenmanager import Screen
import os
import sys
modelPath = os.path.abspath("../../voiva")
sys.path.append(modelPath)
from vapp.wm import WindowManager

class CreateWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)