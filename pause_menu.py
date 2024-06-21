from ursina import *

class PauseMenu(Entity):
    def __init__(self):
        super().__init__(parent = camera.ui, ignore_paused = True)

        self.pause_menu = Entity(parent = self, enabled = True)
        self.player = None
        self.main_menu = None

        def reset():
            self.pause_menu.disable()
            self.player.position = (0, 5, 0)
            self.player.enable()
            mouse.locked = True
            self.player.time.enable()
            self.player.time_running = True

        def resume():
            self.player.enable()
            mouse.locked = True
            self.pause_menu.disable()
            self.player.time.enable()
            self.player.time_running = True

        resume_button = Button(text = "CONTINUE", color = color.black, scale_y = 0.1, scale_x = 0.3, y = 0.12, parent = self.pause_menu)
        reset_button = Button(text = "RESTART", color = color.black, scale_y = 0.1, scale_x = 0.3, y = 0, parent = self.pause_menu)
        quit_button = Button(text = "QUIT", color = color.black, scale_y = 0.1, scale_x = 0.3, y = -0.12, parent = self.pause_menu)
        quit_button.on_click = application.quit
        reset_button.on_click = Func(reset)
        resume_button.on_click = Func(resume)
