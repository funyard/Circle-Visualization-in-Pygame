#!/usr/bin/pypy3

import pygame
import sys
import utils
import string


def main() -> None:

    pygame.init()

    # VARS
    WIDTH, HEIGHT = 800, 600
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 240)
    GRAY = (15, 15, 15)
    FONT = pygame.font.Font(None, 60)

    # Initialise screen

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Midpoint circle visualization")

    # Fill background
    background = pygame.Surface(screen.get_size())
    background.fill(WHITE)

    # Create main menu
    start_button = pygame.Rect(400 - 200 / 2, 440, 200, 100)
    filled_circle_button = pygame.Rect(150, 300, 200, 100)
    hollow_circle_button = pygame.Rect(450, 300, 200, 100)
    radius_input_field_rect = InputBox(screen, 150, 200, 500, 60, BLACK)
    text_surface = FONT.render("Midpoint circle visualization", True, BLACK)

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    screen.blit(text_surface, (120, 100))

    pygame.draw.rect(screen, BLUE, start_button)
    pygame.draw.rect(screen, GRAY, filled_circle_button)
    pygame.draw.rect(screen, GRAY, hollow_circle_button)
    radius_input_field_rect.draw()

    # Creates lists with coordinates for each circle
    list_of_rect_coords = utils.midpoint_circle_draw(WIDTH, HEIGHT, 200)
    list_of_filled_rect_coords = utils.fill_circle(WIDTH, HEIGHT, 200)

    # Event loop
    while True:
        # For quiting
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_coords = pygame.mouse.get_pos()
                # if mouse_coords[1] < 300:
                #     for el in list_of_rect_coords:
                #         pygame.draw.rect(
                #             screen, BLACK, pygame.Rect(int(el[0]), int(el[1]), 2, 2)
                #         )
                # else:
                #     for el in list_of_filled_rect_coords:
                #         pygame.draw.rect(
                #             screen, BLACK, pygame.Rect(int(el[0]), int(el[1]), 1, 1)
                #         )
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RETURN:
                    radius = radius_input_field_rect.string_of_keys
                    radius_input_field_rect.clear()

                if event.key == pygame.K_BACKSPACE:
                    radius_input_field_rect.clear_char()

                if event.unicode in string.digits:
                    radius_input_field_rect.update(event.unicode)

        # Loops through every coordinates from list to draw a hollow circle

        # TODO Create a way to choose which circle to draw

        # Loops through every coordinates from list to draw a filled circle

        # for el in list_of_filled_rect_coords:
        #    pygame.draw.rect(screen, BLACK, pygame.Rect(int(el[0]), int(el[1]), 1, 1))

        pygame.display.update()


class InputBox:
    def __init__(self, surface, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.box = pygame.Rect(self.x, self.y, self.width, self.height)
        self.surface = surface
        self.color = color
        self.string_of_keys = ""
        self.font = pygame.font.Font(None, 50)

    def draw(self):
        pygame.draw.rect(self.surface, self.color, self.box, 2)

    def update(self, key):
        if key in string.digits:
            self.string_of_keys += key

        self.surface.blit(
            self.font.render(self.string_of_keys, False, (0, 0, 0)),
            (self.x + 10, self.y + 15),
        )
        pygame.display.update()

    def clear(self, clear_string=True):
        self.surface.blit(
            self.font.render(self.string_of_keys, False, (255, 255, 255)),
            (self.x + 10, self.y + 15),
        )
        if clear_string:
            self.string_of_keys = ""
        pygame.display.update()

    def clear_char(self):
        self.clear(clear_string=False)
        self.string_of_keys = self.string_of_keys[:-1]
        self.update(self.string_of_keys)


if __name__ == "__main__":
    main()
