from kivy.app import App
from kivy.config import Config
from kivy.uix.widget import Widget

Config.set("graphics", "fullscreen", 0)
Config.set("graphics", "width", 1024)
Config.set("graphics", "height", 600)
Config.write()


class MainWidget(Widget):
    pass


class PLK(App):
    pass


if __name__ == '__main__':
    PLK().run()
