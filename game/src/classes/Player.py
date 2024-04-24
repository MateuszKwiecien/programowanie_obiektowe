import pygame
import math

from classes.Trail import Trail
from constants import size, player, colors


class Player:
    def __init__(self, color: str):
        self.color = colors[color]
        self.x = 50
        self.y = 50
        self.size = size['player']
        self.rotation = 0
        self.trail = Trail(color)


    def move(self):
        self.x += math.sin(self.rotation) * player["speed"]
        self.y += math.cos(self.rotation) * player["speed"]

        self.trail.addPoint(self.x, self.y)

    def rotate(self, right = True):
        if right: self.rotation += player["rotation"]
        elif not right: self.rotation -= player["rotation"]

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)
        self.checkCollision(screen)

    def checkCollision(self, screen):
        color = screen.get_at((int(self.x), int(self.y)))
        print(color)


    
