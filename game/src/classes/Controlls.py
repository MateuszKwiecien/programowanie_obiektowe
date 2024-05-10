import pygame

class Controlls:
    def __init__(self, player) -> None:
        self.player = player


    def handleClick(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT] and self.player.direction != "right" and self.player.direction != "left":
            self.player.changeDirection("left")
            

        if keys[pygame.K_RIGHT] and self.player.direction != "left" and self.player.direction != "right":
            self.player.changeDirection("right")

        if keys[pygame.K_UP] and self.player.direction != "down" and self.player.direction != "up":
            self.player.changeDirection("up")

        if keys[pygame.K_DOWN] and self.player.direction != "up" and self.player.direction != "down":
            self.player.changeDirection("down")
 



