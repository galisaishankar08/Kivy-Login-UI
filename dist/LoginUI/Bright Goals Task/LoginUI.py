from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen

Window.size = (920, 650)

KV = """

ScreenManager:
    LoginScreen:
    HomeScreen:

<LoginScreen>:
    name: 'login'
    canvas.before:
        Color:
            rgba: 227/255, 235/255, 254/255, 1
        Rectangle:
            pos: self.pos
            size: self.size
    
    MDCard:
        size_hint: None, None
        size: 500, 330
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        elevation: 30
        padding: 10
        spacing: 20
        orientation: 'vertical'
        md_bg_color: 0/255, 165/255, 86/255, 1
        
        MDIcon:
            icon: 'close'
            font_size : 30
            halign: 'right'
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            padding_y: -5
            
        
        MDLabel:
            id: login_label
            text: 'App Login'
            font_size: 22
            halign: 'center'
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            bold: True
            size_hint_y: None
            height: self.texture_size[1]
            
        MDCard:
            size_hint: None, None
            size: 420, 40
            radius: 10
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            
            MDTextFieldRect:
                id: email
                color_mode: 'custom'
                line_color_focus: 0, 0, 0, 1
                hint_text: "Enter Email..."
                text_color: 40/255, 40/255, 40/255, 1
                font_size:"20dp"
        
        MDCard:
            size_hint: None, None
            size: 420, 40
            radius: 10
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            
            MDTextFieldRect:
                id: password
                color_mode: 'custom'
                line_color_focus: 0, 0, 0, 1
                hint_text: "Enter Password..."
                text_color: 40/255, 40/255, 40/255, 1
                font_size:"20dp"
                password: True
        
        MDCard:
            size_hint: None, None
            size: 420, 40
            spacing: 20
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            md_bg_color: 0/255, 165/255, 86/255, 1
            
            CurvedButton:
                size_hint: None, None
                size: 250, 40
                text: "Register Account"

            CurvedButton:
                size_hint: None, None
                size: 150, 40
                text: "Login"
                
        MDLabel:
            id: login_label
            text: 'Forgot password?'
            font_size: 18
            halign: 'center'        
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1        
            size_hint_y: None
            height: self.texture_size[1]
            padding_y: 10
            
    MDLabel:
        id: login_label
        text: '© 2022 | GSS All Right Reserved.'
        font_size: 18
        theme_text_color: "Custom"
        text_color: 0, 0, 0, .5
        halign: 'center'                
        size_hint_y: None
        height: self.texture_size[1]
        padding_y: 20
        
<CurvedButton@Button>:
    background_color: (0, 0, 0, 0)
    background_normal: ''
    font_size: 22
    canvas.before:
        Color: 
            rgba: (40/255, 40/255, 40/255, 1)
                
        RoundedRectangle:
            size:self.size
            pos: self.pos
            radius: [10]
        
        
<HomeScreen>:
    name: 'home'

"""


class LoginScreen(Screen):
    pass


class HomeScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(LoginScreen(name='login'))
sm.add_widget(HomeScreen(name='home'))


class GSSApp(MDApp):
    def build(self):
        Window.clearcolor = (227/255, 235/255, 254/255, 1)
        return Builder.load_string(KV)


if __name__ == '__main__':
    GSSApp().run()
