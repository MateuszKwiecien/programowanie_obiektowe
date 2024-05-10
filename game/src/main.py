import pygame
import sys
from constants import colors, size, game
from classes.Controlls import Controlls
from classes.Player import Player

# Initialize Pygame

def main():
    pygame.init()
    player1 = Player("red", 0)
    controlls = Controlls(player1)


    pygame.display.set_caption("My Pygame Project")
    # Set up window and helper surfaces
    WIDTH, HEIGHT = size["plane"]["width"], size["plane"]["height"]
    screen = pygame.display.set_mode((WIDTH, HEIGHT)) # default screen
    base_surface = pygame.Surface((WIDTH, HEIGHT))
    base_surface.set_colorkey(colors["white"])
    base_surface.fill(colors["white"])

    trail_surface = pygame.Surface((WIDTH, HEIGHT))
    trail_surface.set_colorkey(colors["white"])
    trail_surface.fill(colors["white"])

    player1.base.draw(base_surface)



    # Main game loop
    running = True
    clock = pygame.time.Clock()
    while running:
        clock.tick(60)
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
        
        player1.move()

        # Clear the screen
        controlls.handleClick()
        screen.fill(colors["white"])
        
        player1.checkCollision(trail_surface)
        
        player1.trail.draw(trail_surface)
        screen.blit(trail_surface, (0,0))
        screen.blit(base_surface, (0,0))
        player1.draw(screen)
        
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()
    sys.exit()


main()