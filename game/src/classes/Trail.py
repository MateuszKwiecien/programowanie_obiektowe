import pygame
from constants import colors, trail

class Trail:
    def __init__(self, color: str):
        self.color = colors[color+"-trail"]
        self.points = {}
        self.lastPoints = []

    def addPoint(self, x, y):
        self.points[x] = y
        self.lastPoints.append((x,y))

    def resetPoints(self):
        self.points = []

    def draw(self, screen):
        if len(self.lastPoints) < 2: return

        pygame.draw.line(screen, self.color, self.lastPoints[0], self.lastPoints[1], trail["width"])
        self.lastPoints.pop(0)