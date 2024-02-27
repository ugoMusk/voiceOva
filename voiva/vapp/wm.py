from kivy.uix.screenmanager import ScreenManager, NoTransition

class WindowManager(ScreenManager):
    def switch_to_create_screen(self):
        self.transition = NoTransition()
        self.current = 'create'
    
    def switch_to_home_screen(self):
        self.transition = NoTransition()
        self.current = 'home'

    def switch_to_docs_screen(self):
        self.transition = NoTransition()
        self.current = 'docs'
