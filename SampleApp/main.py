from kivy.config import Config
Config.set('graphics', 'rotation', '0')  # This should be set to 0 for normal orientation
    
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, NoTransition

# Load KV files
Builder.load_file('kv/home.kv')
Builder.load_file('kv/settings.kv')
Builder.load_file('kv/profile.kv')
Builder.load_file('kv/cart.kv')

from screens.home import homeScreen
from screens.settings import settingsScreen
from screens.profile import profileScreen
from screens.cart import cartScreen

class MainApp(App):

    def build(self):
        sm = ScreenManager(transition=NoTransition())
        home_screen = homeScreen(name='home')
        sm.add_widget(home_screen)
        settings_screen = settingsScreen(name='settings')
        sm.add_widget(settings_screen)
        profile_screen = profileScreen(name='profile')
        sm.add_widget(profile_screen)
        cart_screen = cartScreen(name='cart')
        sm.add_widget(cart_screen)
        sm.current = 'home'
        return sm

if __name__ == '__main__':
    MainApp().run()