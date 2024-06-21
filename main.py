from ursina import *
from player import Player
from block import *
import pygame

from Levels.level01 import Level01
from Levels.level02 import Level02


from main_menu import MainMenu
from pause_menu import PauseMenu

application.development_mode = True

# App/Window
app = Ursina(borderless = False)

window.title = "Parkour"
window.fps_counter.disable()

window.exit_button = False

normalSpeed = 2
boostSpeed  = 3

normalJump = 0.3

# Player
player = Player("cube", (0, 10, 0), "box", controls="wasd")
player.SPEED = normalSpeed
player.jump_height = normalJump
player.disable()

mouse.locked = False

m = MainMenu()
m.player = player



sky = Sky(texture = "assets/sky4")

# Lighting
PointLight(parent = camera, position = (0, 10, -1.5), color = color.white)
AmbientLight(color = color.rgba(100, 100, 100, 0.1))

level01 = Level01()
level01.player = player


def reset_player():
    player.position = (0, 5, 0)
    player.SPEED = normalSpeed
    player.jump_height = normalJump
    camera.rotation_z = 0

def input(key):
    if key == "escape":
        mouse.locked = False
        player.disable()
        player.time_running = False
        player.time.disable()
        
        p = PauseMenu()
        p.player = player

def update():
    # Stops the player from falling forever
    if player.position.y <= -50:
        player.position = Vec3(0, 5, 0)
        player.SPEED = normalSpeed
        player.jump_height = normalJump
        camera.rotation_z = 0

    # Restart the level
    if held_keys["g"]:
        player.position = Vec3(0, 5, 0)
        player.SPEED = normalSpeed
        player.jump_height = normalJump
        camera.rotation_z = 0
    
   
        

       

    ray = raycast(player.position, player.down, distance = 2, ignore = [player, ])

    if ray.entity == Level01.finishBlock_1:
        Level02.enable()
        Level01.disable()
        reset_player()
    
    if ray.entity == Level02.finishBlock_2:
        m.main_menu.enable()
        player.disable()
        mouse.locked = False
        Level01.enable()
        Level02.disable()
        pygame.mixer.init()
        pygame.mixer.music.load("./assets/german.mp3") 
        pygame.mixer.music.play(-1,0.0)
        reset_player()

    
    



app.run()
