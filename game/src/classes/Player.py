import pygame
import math

from constants import size, player

class Player:
    def __init__(self, color: str):
        self.color = color
        self.x, self.y = player['defaultPosition']
        self.size = size['player']
        self.rotation = 0

    def move(self):
        self.x += math.sin(self.rotation) * player["speed"]
        self.y += math.cos(self.rotation) * player["speed"]

    def rotate(self, right = True):
        if right: self.rotation += player["rotation"]
        elif not right: self.rotation -= player["rotation"]

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)


    
