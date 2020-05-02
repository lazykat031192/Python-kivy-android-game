from kivy.app import App
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.widget import Widget
from kivy.graphics import Line
from kivy.clock import Clock
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ListProperty
from functools import partial
from kivy.properties import NumericProperty
from kivy.properties import OptionProperty
import random
from kivy.core.audio import SoundLoader
from kivy.uix.widget import Widget
import time

class FourthScreen(Screen):
    def __init__(self, **kwargs): #self o day la screen nen phai add them layout
        super(FourthScreen, self).__init__(**kwargs)
        self.button=[]
        self.count=0
        self.buttons=[]
        self.time=[]
        #Clock.schedule_interval(self.flash, 5)
        #self.reset(self.result=True)
    def on_enter(self):
        Clock.schedule_interval(self.flash, 0.6) #sau khi an play thi moi bat dau 
        
    def flash(self,dt):
        y=list(self.ids.keys())
        x=y[self.count]
        self.ids[x].state = 'down'
        Clock.schedule_once(partial(self.setnormal,x), 0.5)  #neu x cung thuoc def setnormal thi phai declare x 
        self.count =self.count+random.randint(5,10)
        self.button.append(x)
        if self.count >=36:  #>=4 thi loop se ngat
            # end the interval scheduling
            return False
        else:
            return True
            #return self.button
    def setnormal(self,x,dt):
        self.ids[x].state = 'normal'   
        print(self.button)
        
    def on_touch_down(self,touch):
        for i in range (1,37):
            if self.ids['butt'+str(i)].collide_point(*touch.pos):
                timeout=0
                self.buttons.append('butt'+str(i))
                timeout+=time.perf_counter()
                self.time.append(timeout)
                print(self.buttons)
                print(self.time[-1]-self.time[0])
        Clock.schedule_once(self.result, 7) #problem is here
        
        if self.ids.next.collide_point(*touch.pos):
            self.manager.current='fourth'
            Clock.unschedule(self.result)
            self.ids.next.text= ''
            self.reset()
        elif self.ids.again.collide_point(*touch.pos):
            self.manager.current='fourth'
            self.ids.again.text= ''
            Clock.unschedule(self.result)  #unschedule clock để chữ not corect try again không hiển thị mỗi 3s vì đã có touch down, chỉ có self.buttons,... reset còn touch thì chưa reset nên cần unschdule
            self.reset()
            
        if self.ids.back.collide_point(*touch.pos):
            self.manager.current='main'
        
    def result(self,dt):
       if self.button!=self.buttons or (self.time[-1]-self.time[0])>7:
            self.ids.again.text='not correct, try again'
       else:
            self.ids.next.text='next'
            
    def reset(self):
        self.button=[]
        self.count=0
        self.buttons=[]
        self.time=[]
        timeout=0
        self.on_enter()
    