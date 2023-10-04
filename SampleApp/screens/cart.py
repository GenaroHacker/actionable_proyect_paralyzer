from kivy.uix.screenmanager import Screen
from utils.cart.view_cart import view_cart
from utils.cart.checkout import checkout
from utils.cart.apply_coupon import apply_coupon
from utils.cart.estimate_shipping import estimate_shipping

class cartScreen(Screen):
    def go_to_home(self):
        print('Navigating from cart to home')
        self.manager.current = 'home'
    def go_to_settings(self):
        print('Navigating from cart to settings')
        self.manager.current = 'settings'
    def go_to_profile(self):
        print('Navigating from cart to profile')
        self.manager.current = 'profile'
    def go_to_cart(self):
        print('Navigating from cart to cart')
        self.manager.current = 'cart'
    view_cart = staticmethod(view_cart)
    checkout = staticmethod(checkout)
    apply_coupon = staticmethod(apply_coupon)
    estimate_shipping = staticmethod(estimate_shipping)