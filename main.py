import webbrowser
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.graphics import Color, RoundedRectangle
from kivy.animation import Animation

class RoundedButton(Button):
    def __init__(self, **kwargs):
        super(RoundedButton, self).__init__(**kwargs)
        self.background_normal = ''
        self.background_color = (0, 0, 0, 0)
        self.bind(pos=self.update_canvas, size=self.update_canvas)

    def update_canvas(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(*get_color_from_hex('#000000'))
            RoundedRectangle(pos=self.pos, size=self.size, radius=15)

class SplashScreen(Screen):
    def on_enter(self):
        self.ids.splash_img.opacity = 0
        self.ids.welcome_txt.opacity = 0
        self.ids.sub_txt.opacity = 0
        
        anim = Animation(opacity=1, duration=2.5)
        anim.bind(on_complete=self.switch_to_main)
        
        anim.start(self.ids.splash_img)
        anim.start(self.ids.welcome_txt)
        anim.start(self.ids.sub_txt)

    def switch_to_main(self, *args):
        self.manager.current = 'main_screen'

class MainScreen(Screen):
    def open_catalog(self):
        webbrowser.open("https://tetyaasya05.ru")

    def open_info(self):
        webbrowser.open("https://tetyaasya05.ru")

    def open_about(self):
        webbrowser.open("https://tetyaasya05.ru")

    def exit_app(self):
        App.get_running_app().stop()

class MainApp(App):
    def build(self):
        Window.clearcolor = get_color_from_hex('#FFFFFF')
        sm = ScreenManager(transition=FadeTransition(duration=0.8))
        
        splash = SplashScreen(name='splash_screen')
        splash_layout = BoxLayout(orientation='vertical', padding=30, spacing=15)
        
        splash_img = Image(source="logo.png", size_hint=(1, None), height=220, pos_hint={'center_x': 0.5})
        welcome_txt = Label(text="Добро пожаловать!", font_size='28sp', bold=True, color=get_color_from_hex('#000000'), size_hint_y=None, height=50)
        sub_txt = Label(text="Здоровое питание от тети Аси", font_size='15sp', color=get_color_from_hex('#7F7F7F'), size_hint_y=None, height=30)
        
        splash.ids['splash_img'] = splash_img
        splash.ids['welcome_txt'] = welcome_txt
        splash.ids['sub_txt'] = sub_txt
        
        splash_layout.add_widget(splash_img)
        splash_layout.add_widget(welcome_txt)
        splash_layout.add_widget(sub_txt)
        splash.add_widget(splash_layout)
        
        main_scr = MainScreen(name='main_screen')
        main_layout = BoxLayout(orientation='vertical', padding=20, spacing=12)
        
        top_image = Image(source="logo.png", size_hint=(1, None), height=180, pos_hint={'center_x': 0.5})
        version_label = Label(text="Версия приложения: 1.0.0", font_size='14sp', color=get_color_from_hex('#7F7F7F'), size_hint_y=None, height=25)
        
        btn_catalog = RoundedButton(text="Перейти в каталог", font_size='18sp', color=get_color_from_hex('#FFFFFF'), size_hint_y=None, height=55)
        btn_catalog.bind(on_press=lambda x: main_scr.open_catalog())
        
        btn_info = RoundedButton(text="Инфо", font_size='18sp', color=get_color_from_hex('#FFFFFF'), size_hint_y=None, height=55)
        btn_info.bind(on_press=lambda x: main_scr.open_info())
        
        btn_about = RoundedButton(text="О нас", font_size='18sp', color=get_color_from_hex('#FFFFFF'), size_hint_y=None, height=55)
        btn_about.bind(on_press=lambda x: main_scr.open_about())
        
        btn_exit = RoundedButton(text="Выход", font_size='18sp', color=get_color_from_hex('#FFFFFF'), size_hint_y=None, height=55)
        btn_exit.bind(on_press=lambda x: main_scr.exit_app())
        
        main_layout.add_widget(top_image)
        main_layout.add_widget(version_label)
        main_layout.add_widget(btn_catalog)
        main_layout.add_widget(btn_info)
        main_layout.add_widget(btn_about)
        main_layout.add_widget(btn_exit)
        main_scr.add_widget(main_layout)
        
        sm.add_widget(splash)
        sm.add_widget(main_scr)
        
        return sm

if __name__ == '__main__':
    MainApp().run()
