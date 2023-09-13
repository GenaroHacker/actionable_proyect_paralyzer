from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView

from kivy.uix.screenmanager import RiseInTransition

class ScreenB(Screen):
    def __init__(self, **kwargs):
        super(ScreenB, self).__init__(**kwargs)
        layout = GridLayout(cols=1, padding=10, spacing=10, size_hint=(1, None), width=500)
        layout.bind(minimum_height=layout.setter('height'))
        btn = Button(text="Go to Screen A", size=(480, 40), size_hint=(1, None))
        btn.bind(on_press=self.change_screen)
        layout.add_widget(btn)
        root = ScrollView(size_hint=(1, 1), size=(500, 320), pos_hint={'center_x': .5, 'center_y': .5}, do_scroll_x=False)
        root.add_widget(layout)
        self.add_widget(root)

    def change_screen(self, instance):
        self.manager.transition = RiseInTransition()
        self.manager.current = "screen_a"
