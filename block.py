from ursina import *

# Normal Block Class
class NormalBlock(Entity):
    def __init__(self, position = (0, 0, 0), rotation = (0, 0, 0)):
        super().__init__(
            model = "cube",
            scale = Vec3(8, 0.8, 9),
            color = "#8ab4f8",
            collider = "box",
            texture = "white_cube",
            position = position,
            rotation = rotation,
        )

class NormalBlock1(Entity):
    def __init__(self, position = (0, 0, 0), rotation = (0, 0, 0)):
        super().__init__(
            model = "cube",
            scale = Vec3(10, 0.8, 3),
            color = "#00000000",
            collider = "box",
            opacity = 0,
            texture = "white_cube",
            position = position,
            rotation = rotation,
        )

class NormalBlock3(Entity):
    def __init__(self, position = (0, 0, 0), rotation = (0, 0, 0)):
        super().__init__(
            model = "cube",
            scale = Vec3(3, 0.8, 3),
            color = "#AFFF3C",
            collider = "box",
            texture = "white_cube",
            position = position,
            rotation = rotation,
        )

class FakeBlock3(Entity):
    def __init__(self, position = (0, 0, 0)):
        super().__init__(
            model = "cube",
            scale = Vec3(3, 0.8, 3),
            color = "#AFFF3C",
            texture = "white_cube",
            position = position,
        )



# Jump Block Class
class JumpBlock(Entity):
    def __init__(self, position = (0, 0, 0)):
        super().__init__(
            model = "cube",
            scale = Vec3(10, 0.8, 10),
            color = "#FF8B00",
            collider = "box",
            texture = "white_cube",
            position = position,
        )

class JumpBlock2(Entity):
    def __init__(self, position = (0, 0, 0)):
        super().__init__(
            model = "cube",
            scale = Vec3(10, 0.8, 10),
            color = "#8ab4f8",
            collider = "box",
            texture = "white_cube",
            position = position,
        )

class JumpBlock3(Entity):
    def __init__(self, position = (0, 0, 0)):
        super().__init__(
            model = "cube",
            scale = Vec3(10, 0.8, 10),
            color = "#8ab4f8",
            collider = "box",
            texture = "white_cube",
            position = position,
        )

# Speed Block Class
class SpeedBlock(Entity):
    def __init__(self, position = (0, 0, 0), scale = (3, 0.5,20)):
        super().__init__(
            model = "cube",
            scale = scale,
            color = "#53FFF5",
            collider = "box",
            texture = "white_cube",
            position = position,
        )

# Slow Block Class
class SlowBlock(Entity):
    def __init__(self, position = (0, 0, 0)):
        super().__init__(
            model = "cube",
            scale = Vec3(3, 0.5, 15),
            color = "#FF453F",
            collider = "box",
            texture = "white_cube",
            position = position,
        )

class WeirdBlock(Entity):
    def __init__(self, position = (0, 0, 0)):
        super().__init__(
            model = "cube",
            scale = Vec3(3, 0.5, 15),
            color = "#7116FE",
            collider = "box",
            texture = "white_cube",
            position = position,
        )

class Wall(Entity):
    def __init__(self, position = (0, 0, 0)):
        super().__init__(
            model = "cube",
            scale = (5, 4, 1),
            color = "#AFFF3C",
            collider = "box",
            texture = "white_cube",
            position = position,
            rotation = (0, 0, 90)
        )

class MovingBlock(Entity):
    def __init__(self, position = (0, 0, 0)):
        super().__init__(
            model = "cube",
            scale = Vec3(3, 0.8, 3),
            color = "#2D49FB",
            collider = "box",
            texture = "white_cube",
            position = position,
        )

class FakeBlock(Entity):
    def __init__(self, position = (0, 0, 0)):
        super().__init__(
            model = "cube",
            scale = Vec3(8, 0.8, 9),
            color = "#8ab4f8",
            texture = "white_cube",
            position = position,
        )

class JumpFakeBlock(Entity):
    def __init__(self, position = (0, 0, 0)):
        super().__init__(
            model = "cube",
            scale = Vec3(10, 0.8, 10),
            color = "#FF8B00",
            texture = "white_cube",
            position = position,
        )

class FakeBlock2(Entity):
    def __init__(self, position = (0, 0, 0)):
        super().__init__(
            model = "cube",
            scale = Vec3(10, 0.8, 10),
            color = "#CACACA",
            texture = "white_cube",
            position = position,
        )

class StartBlock(Entity):
    def __init__(self, position = (0, 0, 0)):
        super().__init__(
            model = "cube",
            scale_x = 10,
            scale_z = 10,
            color = "#CACACA",
            collider = "box",
            texture = "white_cube",
            position = position,
        )

class EndBlock(Entity):
    def __init__(self, position = (0, 0, 0)):
        super().__init__(
            model = "cube",
            scale_x = 10,
            scale_z = 10,
            color = "#CACACA",
            collider = "box",
            texture = "white_cube",
            position = position,
        )
