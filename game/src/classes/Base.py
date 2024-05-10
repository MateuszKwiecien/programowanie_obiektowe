import pygame

from constants import colors, base

class Base:
    def __init__(self, color: str, initX: int, initY: int):
        self.color = colors[color+"-base"]
        self.initX = initX
        self.initY = initY
        self.initW = base["initial"]["width"]
        self.initH = base["initial"]["height"]

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, [self.initX, self.initY, self.initW, self.initH])

    def expand(self, screen, traiPoints):
        pass