from kivy.uix.screenmanager import Screen
from utils.settings.payment_methods import payment_methods
from utils.settings.shipping_address import shipping_address
from utils.settings.notification_preferences import notification_preferences
from utils.settings.account_settings import account_settings
from utils.settings.volume_up import volume_up
from utils.settings.volume_down import volume_down

class settingsScreen(Screen):
    def go_to_home(self):
        print('Navigating from settings to home')
        self.manager.current = 'home'
    def go_to_settings(self):
        print('Navigating from settings to settings')
        self.manager.current = 'settings'
    def go_to_profile(self):
        print('Navigating from settings to profile')
        self.manager.current = 'profile'
    def go_to_cart(self):
        print('Navigating from settings to cart')
        self.manager.current = 'cart'
    payment_methods = staticmethod(payment_methods)
    shipping_address = staticmethod(shipping_address)
    notification_preferences = staticmethod(notification_preferences)
    account_settings = staticmethod(account_settings)
    volume_up = staticmethod(volume_up)
    volume_down = staticmethod(volume_down)