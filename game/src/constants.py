import math

game = {
    "delay": 100
}

colors = {
    "white": (255,255,255),
    "red": (255, 0, 0),
    "red-base": (230, 0, 0),
    "red-trail": (200, 0, 0)
}

size = {
    "plane": {
        "width": 800,
        "height": 600
    },
    "player": 10
}

player = {
    "speed": 0.05,
    "rotation": (math.pi / 180) / 10
}

base = {
    "initial": {
        "width": 50,
        "height": 50
    }
}

trail = {
    "width": 5
}

