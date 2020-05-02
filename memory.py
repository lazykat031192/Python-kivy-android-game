from kivy.app import App
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.widget import Widget
from kivy.graphics import Line
from kivy.core.audio import SoundLoader
from kivy.uix.label import Label
# __version__ = '1.0'
Builder.load_file('screenmanagement.kv')
Builder.load_file('introduction.kv')
Builder.load_file('play.kv')
#Builder.load_file('next.kv')
#Builder.load_file('again.kv')


class MainScreen(Screen):
    pass

class SecondScreen(Screen):
    pass   

class ThirdScreen(Screen):
    pass

class FourthScreen(Screen):
    pass

class Exit(Label):
    pass

class ScreenManagement(ScreenManager):
    pass

class MemoryApp(App):
    def build(self):
        self.sound=SoundLoader.load('News_Room_News.wav')
        self.sound.play()
        self.sound.loop=True
        return ScreenManagement()
    
if __name__=="__main__":
    MemoryApp().run()