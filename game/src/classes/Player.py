import pygame
import math

from classes.Trail import Trail
from classes.Base import Base
from constants import size, player, colors, base


class Player:
    def __init__(self, color: str, playerNum: int):
        basePos = base["positions"][playerNum]
        self.color = colors[color]
        self.x, self.y = basePos
        self.size = size['player']
        self.direction = "right"
        self.alive = True
        self.base = Base(color, basePos[0], basePos[1])
        self.trail = Trail(color)
        self.colC = 0
        self.atBase = True


    def move(self):
        match self.direction:
            case "down":
                self.y += player["speed"]
            case "up":
                self.y -= player["speed"]
            case "right":
                self.x += player["speed"]
            case "left":
                self.x -= player["speed"]
        if not self.atBase:
            self.trail.addPoint(self.x, self.y)

    def changeDirection(self, direction: str):
        self.direction = direction

        if not self.atBase:
            self.trail.addRotationPoint(self.x, self.y)


    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)

    def checkCollision(self, trail_surface):
        trail_color = trail_surface.get_at((int(self.x), int(self.y)))
        # base_color = base_surface.get_at((int(self.x)))
        if trail_color != (255, 255, 255):
            self.colC += 1
        else:
            self.colC = 0
            self.atBase = False

        if self.colC > 2:
            print("collision")
    


    
