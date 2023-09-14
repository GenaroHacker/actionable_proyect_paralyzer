from kivy.lang import Builder
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

# Load KV files
Builder.load_file('a.kv')
Builder.load_file('b.kv')

from a import AScreen
from b import BScreen

class MainApp(App):

    def build(self):
        sm = ScreenManager()
        a_screen = AScreen(name='a')
        b_screen = BScreen(name='b')
        sm.add_widget(a_screen)
        sm.add_widget(b_screen)
        sm.current = 'a'  # Set initial screen
        return sm

if __name__ == '__main__':
    MainApp().run()
