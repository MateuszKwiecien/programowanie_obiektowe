import pygame
from constants import colors, trail

class Trail:
    def __init__(self, color: str):
        self.color = colors[color+"-trail"]
        self.points = []

    def addPoint(self, x, y):
        self.points.append((x,y))

    def resetPoints(self):
        self.points = []

    def draw(self, screen):
        if len(self.points) < 2: return

        lastPoints = self.points[-2:]
        pygame.draw.line(screen, self.color, lastPoints[0], lastPoints[1], trail["width"])