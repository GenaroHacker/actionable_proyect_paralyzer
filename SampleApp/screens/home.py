from kivy.uix.screenmanager import Screen
from utils.home.browse_products import browse_products
from utils.home.search import search
from utils.home.view_promotions import view_promotions
from utils.home.recommendations import recommendations

class homeScreen(Screen):
    def go_to_home(self):
        print('Navigating from home to home')
        self.manager.current = 'home'
    def go_to_settings(self):
        print('Navigating from home to settings')
        self.manager.current = 'settings'
    def go_to_profile(self):
        print('Navigating from home to profile')
        self.manager.current = 'profile'
    def go_to_cart(self):
        print('Navigating from home to cart')
        self.manager.current = 'cart'
    browse_products = staticmethod(browse_products)
    search = staticmethod(search)
    view_promotions = staticmethod(view_promotions)
    recommendations = staticmethod(recommendations)