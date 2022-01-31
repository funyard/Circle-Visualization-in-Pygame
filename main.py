#!/usr/bin/pypy3

import pygame
import sys
import utils


def main() -> None:

    # VARS
    WIDTH, HEIGHT = 800, 600
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Midpoint circle visualization")

    # Fill background
    background = pygame.Surface(screen.get_size())
    background.fill(WHITE)

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Creates lists with coordinates for each circle
    list_of_rect_coords = utils.midpoint_circle_draw(WIDTH, HEIGHT, 200)
    list_of_filled_rect_coords = utils.fill_circle(WIDTH, HEIGHT, 200)

    # Event loop
    while True:
        # For quiting
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Loops through every coordinates from list to draw a hollow circle
        
        #TODO Create a way to choose which circle to draw
        
        for el in list_of_rect_coords:
            pygame.draw.rect(screen, BLACK, pygame.Rect(int(el[0]), int(el[1]), 2, 2))

        # Loops through every coordinates from list to draw a filled circle
        
        # for el in list_of_filled_rect_coords:
        #    pygame.draw.rect(screen, BLACK, pygame.Rect(int(el[0]), int(el[1]), 1, 1))

        pygame.display.update()


if __name__ == "__main__":
    main()
