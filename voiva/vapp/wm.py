from kivy.uix.screenmanager import ScreenManager, NoTransition
from engine.tts import VoivaTTS
import threading

class WindowManager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text_to_speech = VoivaTTS()

    def switch_to_create_screen(self):
        self.transition = NoTransition()
        self.current = 'create'
    
    def switch_to_home_screen(self):
        self.transition = NoTransition()
        self.current = 'home'

    def switch_to_docs_screen(self):
        self.transition = NoTransition()
        self.current = 'docs'

    def translate_text_to_speech(self):
        user_input_text = self.ids.user_input.text
        threading.Thread(target=self.run_text_to_speech, args=(user_input_text,)).start()
        
    def run_text_to_speech(self, text):
        output = self.text_to_speech.vtts(text)
        self.ids.output_label.text = output

    # def translate_text_to_speech(self):
    #     user_input_text = self.ids.user_input.text
    #     self.ids.output_label.text = self.text_to_speech.vtts(user_input_text)

    # def translate_text_to_speech(self):
    #     # self.transition = NoTransition()
    #     # self.current = 'create'
    #     user_input_text = self.ids.user_input.text
    #     if user_input_text:
    #         engine = pyttsx3.init()
    #         engine.say(user_input_text)
    #         engine.runAndWait()
    #         self.ids.output_label.text = "Text translated to speech successfully!"
    #     else:
    #         self.ids.output_label.text = "Please enter some text before translating."
