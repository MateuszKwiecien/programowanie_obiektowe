import pygame
import sys
from constants import colors, size
from classes.Controlls import Controlls
from classes.Player import Player

# Initialize Pygame

def main():
    pygame.init()
    player1 = Player(colors['red'])
    controlls = Controlls(player1)

    # Set up window
    WIDTH, HEIGHT = size["plane"]["width"], size["plane"]["height"]
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("My Pygame Project")


    # Main game loop
    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
        controlls.handleClick()
        
        # Clear the screen
        screen.fill(colors["white"])
        
        # Draw a rectangle // example:
        player1.draw(screen)
        player1.move()
        
        # Update the display
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()
    sys.exit()


main()