import pygame

class Controlls:
    def __init__(self, player) -> None:
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.player = player

    def movePlayer(self):
        if self.right:
            self.player.rotate(False)
        if self.left:
            self.player.rotate()

    def handleClick(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT]:

            self.left = True
        else:
            self.left = False
        if keys[pygame.K_RIGHT]:
            self.right = True
        else:
            self.right = False
        if keys[pygame.K_UP]:
            self.up = True
        else:
            self.up = False
        if keys[pygame.K_DOWN]:
            self.down = True
        else:
            self.down = False

        self.movePlayer()


