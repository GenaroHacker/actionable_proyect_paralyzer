#!/bin/bash

# Create main.py
echo "from kivy.lang import Builder
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
    MainApp().run()" > main.py

# Create a.py
echo "from kivy.uix.screenmanager import Screen

class AScreen(Screen):
    pass" > a.py

# Create a.kv
echo "<AScreen>:
    ScrollView:
        do_scroll_x: False
        GridLayout:
            cols: 1
            size_hint_y: None
            height: self.minimum_height
            canvas.before:
                Color:
                    rgb: 1, 0, 0
                Rectangle:
                    pos: self.pos
                    size: self.size
            Button:
                text: 'Go to Screen B'
                size_hint_y: None
                height: 40
                on_press: root.manager.current = 'b'" > a.kv

# Create b.py
echo "from kivy.uix.screenmanager import Screen

class BScreen(Screen):
    pass" > b.py

# Create b.kv
echo "<BScreen>:
    ScrollView:
        do_scroll_x: False
        GridLayout:
            cols: 1
            size_hint_y: None
            height: self.minimum_height
            canvas.before:
                Color:
                    rgb: 0, 1, 0
                Rectangle:
                    pos: self.pos
                    size: self.size
            Button:
                text: 'Go to Screen A'
                size_hint_y: None
                height: 40
                on_press: root.manager.current = 'a'" > b.kv

echo "All files have been created."
