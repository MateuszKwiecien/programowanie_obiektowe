import pygame
from constants import colors, trail

class Trail:
    def __init__(self, color: str):
        self.color = colors[color+"-trail"]
        self.lastPoints = []
        self.rotationPoints = []

    def addPoint(self, x, y):
        self.lastPoints.append((int(x),int(y)))

    def addRotationPoint(self, x, y):
        self.rotationPoints.append((int(x), int(y)))

    def resetPoints(self):
        self.lastPoints = []
        self.rotationPoints = []


    def draw(self, screen):
        if len(self.lastPoints) < 2: return

        pygame.draw.line(screen, self.color, self.lastPoints[0], self.lastPoints[1], trail["width"])
        self.lastPoints.pop(0)