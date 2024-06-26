from ursina import *
import pygame

class MainMenu(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui
        )

        self.main_menu = Entity(parent = self, enabled = True)
        self.player = None

        def start():
            self.player.enable()
            mouse.locked = True
            self.main_menu.disable()
            self.player.time_running = True
            self.background = Entity(parent=self.main_menu,model='quad',color=color.gray,scale=(16, 9, 1),z=-1)

        title = Entity(model = "quad", scale = (0.8, 0.2, 0.2), texture = "assets\parkour_logo_4.png", parent = self.main_menu, y = 0.3)

        start_button = Button(text = "Start", color = color.blue, scale_y = 0.1, scale_x = 0.3, y = -0.1, parent = self.main_menu)
        quit_button = Button(text = "Quit", color = color.red, scale_y = 0.1, scale_x = 0.3, y = -0.22, parent = self.main_menu)
        quit_button.on_click = application.quit
        start_button.on_click = Func(start)
        pygame.mixer.init()
        pygame.mixer.music.load("./assets/german.mp3")
        pygame.mixer.music.play(-1,0.0)
