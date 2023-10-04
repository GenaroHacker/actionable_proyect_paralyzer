from kivy.uix.screenmanager import Screen
from utils.profile.order_history import order_history
from utils.profile.wishlist import wishlist
from utils.profile.edit_profile import edit_profile
from utils.profile.sign_out import sign_out

class profileScreen(Screen):
    def go_to_home(self):
        print('Navigating from profile to home')
        self.manager.current = 'home'
    def go_to_settings(self):
        print('Navigating from profile to settings')
        self.manager.current = 'settings'
    def go_to_profile(self):
        print('Navigating from profile to profile')
        self.manager.current = 'profile'
    def go_to_cart(self):
        print('Navigating from profile to cart')
        self.manager.current = 'cart'
    order_history = staticmethod(order_history)
    wishlist = staticmethod(wishlist)
    edit_profile = staticmethod(edit_profile)
    sign_out = staticmethod(sign_out)