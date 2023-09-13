from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

from a import ScreenA
from b import ScreenB

# Load the .kv files
Builder.load_file('a.kv')
Builder.load_file('b.kv')

class ScreenManagement(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        sm = ScreenManagement()
        sm.add_widget(ScreenA(name="screen_a"))
        sm.add_widget(ScreenB(name="screen_b"))
        return sm

if __name__ == "__main__":
    MainApp().run()
