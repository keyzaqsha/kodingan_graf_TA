from ursina import *
import sys
sys.path.append('../Parkour/')
from block import *

normalSpeed = 2
boostSpeed  = 3
normalJump = 0.3

#Level01
class Level01(Entity):
    def __init__(self):
        super().__init__()
        self.block_1_1 = NormalBlock3((0, 1, 12)) 
        self.block_1_2 = NormalBlock3((0, 1, 20))
        self.block_1_3 = NormalBlock3((0, 1, 28))
        self.block_1_4 = NormalBlock3((0, 1, 36))
        self.block_1_5 = NormalBlock3((0, 1, 44))
        
        self.block_1_6 = NormalBlock3((4, 1, 28))
        self.block_1_7 = NormalBlock3((8, 1, 28))
        self.block_1_8 = NormalBlock3((12, 1, 28))
        self.block_1_9 = NormalBlock3((16, 1, 28))
        self.block_1_10 = NormalBlock3((20, 1, 28))
        
        self.block_1_11 = NormalBlock3((20, 1, 12))
        self.block_1_12 = NormalBlock3((20, 1, 20))
        self.block_1_13 = NormalBlock3((20, 1, 28))
        self.block_1_14 = NormalBlock3((20, 1, 36))
        self.block_1_15 = NormalBlock3((20, 1, 44))
        
        self.block_1_16 = NormalBlock3((30, 1, 12))
        self.block_1_17 = NormalBlock3((30, 1, 20))
        self.block_1_18 = NormalBlock3((30, 1, 28))
        self.block_1_19 = NormalBlock3((30, 1, 36))
        self.block_1_20 = NormalBlock3((30, 1, 44))
        
        self.block_1_21 = NormalBlock3((34, 1, 28))
        self.block_1_22 = NormalBlock3((38, 1, 28))
        self.block_1_23 = NormalBlock3((42, 1, 28))
        self.block_1_24 = NormalBlock3((46, 1, 28))
        
        self.block_1_25 = NormalBlock3((34, 1, 12))
        self.block_1_26 = NormalBlock3((38, 1, 12))
        self.block_1_27 = NormalBlock3((42, 1, 12))
        self.block_1_28 = NormalBlock3((46, 1, 12))
        
        self.block_1_29 = NormalBlock3((34, 1, 44))
        self.block_1_30 = NormalBlock3((38, 1, 44))
        self.block_1_31 = NormalBlock3((42, 1, 44))
        self.block_1_32 = NormalBlock3((46, 1, 44))
        
        self.block_1_33 = NormalBlock3((56, 1, 12))
        self.block_1_34 = NormalBlock3((56, 1, 20))
        self.block_1_35 = NormalBlock3((56, 1, 28))
        self.block_1_36 = NormalBlock3((56, 1, 36))
        self.block_1_37 = NormalBlock3((56, 1, 44))
        
        self.block_1_38 = NormalBlock3((60, 1, 12))
        self.block_1_39 = NormalBlock3((64, 1, 12))
        self.block_1_40 = NormalBlock3((68, 1, 12))
        self.block_1_41 = NormalBlock3((72, 1, 12))
        
        self.block_1_42 = NormalBlock3((80, 1, 12))
        self.block_1_43 = NormalBlock3((80, 1, 20))
        self.block_1_44 = NormalBlock3((80, 1, 28))
        self.block_1_45 = NormalBlock3((80, 1, 36))
        self.block_1_46 = NormalBlock3((80, 1, 44))
        
        self.block_1_47 = NormalBlock3((84, 1, 12))
        self.block_1_48 = NormalBlock3((88, 1, 12))
        self.block_1_49 = NormalBlock3((92, 1, 12))
        self.block_1_50 = NormalBlock3((96, 1, 12))
        
        self.ground_1 = StartBlock()
        self.finishBlock_1 = EndBlock((110, 1, 12))

        self.player = None

    def speed(self):
        self.player.SPEED = normalSpeed

    def disable(self):
       self.block_1_1.disable()
       self.block_1_2.disable()
       self.block_1_3.disable()
       self.block_1_4.disable()
       self.block_1_5.disable()
       self.block_1_6.disable()
       self.block_1_7.disable()
       self.block_1_8.disable()
       self.block_1_9.disable()
       self.block_1_10.disable()
       self.block_1_11.disable()
       self.block_1_12.disable()
       self.block_1_13.disable()
       self.block_1_14.disable()
       self.block_1_15.disable()
       self.block_1_16.disable()
       self.block_1_17.disable()
       self.block_1_18.disable()
       self.block_1_19.disable()
       self.block_1_20.disable()
       self.block_1_21.disable()
       self.block_1_22.disable()
       self.block_1_23.disable()
       self.block_1_24.disable()
       self.block_1_25.disable()
       self.block_1_26.disable()
       self.block_1_27.disable()
       self.block_1_28.disable()
       self.block_1_29.disable()
       self.block_1_30.disable()
       self.block_1_31.disable()
       self.block_1_32.disable()
       self.block_1_33.disable()
       self.block_1_34.disable()
       self.block_1_35.disable()
       self.block_1_36.disable()
       self.block_1_37.disable()
       self.block_1_38.disable()
       self.block_1_39.disable()
       self.block_1_40.disable()
       self.block_1_41.disable()
       self.block_1_42.disable()
       self.block_1_43.disable()
       self.block_1_44.disable()
       self.block_1_45.disable()
       self.block_1_46.disable()
       self.block_1_47.disable()
       self.block_1_48.disable()
       self.block_1_49.disable()
       self.block_1_50.disable()
       self.finishBlock_1.disable()
       self.ground_1.disable()

    def enable(self):
       self.block_1_1.enable()
       self.block_1_2.enable()
       self.block_1_3.enable()
       self.block_1_4.enable()
       self.block_1_5.enable()
       self.block_1_6.enable()
       self.block_1_7.enable()
       self.block_1_8.enable()
       self.block_1_9.enable()
       self.block_1_10.enable()
       self.block_1_11.enable()
       self.block_1_12.enable()
       self.block_1_13.enable()
       self.block_1_14.enable()
       self.block_1_15.enable()
       self.block_1_16.enable()
       self.block_1_17.enable()
       self.block_1_18.enable()
       self.block_1_19.enable()
       self.block_1_20.enable()
       self.block_1_21.enable()
       self.block_1_22.enable()
       self.block_1_23.enable()
       self.block_1_24.enable()
       self.block_1_25.enable()
       self.block_1_26.enable()
       self.block_1_27.enable()
       self.block_1_28.enable()
       self.block_1_29.enable()
       self.block_1_30.enable()
       self.block_1_31.enable()
       self.block_1_32.enable()
       self.block_1_33.enable()
       self.block_1_34.enable()
       self.block_1_35.enable()
       self.block_1_36.enable()
       self.block_1_37.enable()
       self.block_1_38.enable()
       self.block_1_39.enable()
       self.block_1_40.enable()
       self.block_1_41.enable()
       self.block_1_42.enable()
       self.block_1_43.enable()
       self.block_1_44.enable()
       self.block_1_45.enable()
       self.block_1_46.enable()
       self.block_1_47.enable()
       self.block_1_48.enable()
       self.block_1_49.enable()
       self.block_1_50.enable()
       self.finishBlock_1.enable()
       self.ground_1.enable()

    def update(self):
        # Stops the player from falling forever
        if self.player.position.y <= -50:
            self.player.position = Vec3(0, 5, 0)
            self.player.SPEED = normalSpeed
            self.player.jump_height = normalJump
            camera.rotation = (0, 0, 0)

        # Restart the level
        if held_keys["g"]:
            self.player.position = Vec3(0, 5, 0)
            self.player.SPEED = normalSpeed
            self.player.jump_height = normalJump
            camera.rotation = (0, 0, 0)

        # What entity the player hits
        hit = raycast(self.player.position, self.player.down, distance = 2, ignore = [self.player, ])
        
        if self.ground_1.enabled == True:
            if hit.entity == self.block_1_7:
                self.player.jump_height = 0.7
            elif hit.entity != self.block_1_7:
                self.player.jump_height = normalJump

            if hit.entity == self.block_1_9:
                self.player.SPEED = boostSpeed * 1.2
                invoke(self.speed, delay=3)

            if hit.entity == self.finishBlock_1:
                pass