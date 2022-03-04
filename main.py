#!python3

import string
import sys

import pygame
import pygame_widgets
from pygame_widgets.button import Button

import classes
import utils


def main() -> None:
    pygame.init()

    def set_circle_type(value):
        global filled
        filled = value

    # VARS
    global WIDTH, HEIGHT, filled
    filled = None
    WIDTH, HEIGHT = 800, 600
    black = (0, 0, 0)
    white = (255, 255, 255)
    blue = (0, 0, 240)
    gray = (15, 15, 15)
    title_font = pygame.font.Font(None, 60)

    # Initialise screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Midpoint circle visualization")

    # Fill background
    background = pygame.Surface(screen.get_size())
    background.fill(white)

    # Create main menu
    start_button = Button(
        screen,
        int(400 - 200 / 2),
        440,
        200,
        100,
        text="START",
        textColour=white,
        fontsize=34,
        margin=20,
        inactiveColour=blue,
        pressedColour=(20, 20, 90),
        onClick=lambda: utils.start_button_func(
            radius_input_field_rect,
            screen,
            background,
            start_button,
            filled,
            hollow_circle_button,
            filled_circle_button,
        ),
        radius=4,
    )
    filled_circle_button = Button(
        screen,
        150,
        300,
        200,
        100,
        text="FILLED CIRCLE",
        textColour=white,
        fontsize=34,
        margin=20,
        inactiveColour=gray,
        pressedColour=(20, 20, 90),
        onClick=lambda: set_circle_type(True),
        radius=4,
    )
    hollow_circle_button = Button(
        screen,
        450,
        300,
        200,
        100,
        text="HOLLOW CIRCLE",
        textColour=white,
        fontsize=34,
        margin=20,
        inactiveColour=gray,
        pressedColour=(20, 20, 90),
        radius=4,
        onClick=lambda: set_circle_type(False),
    )
    radius_input_field_rect = classes.InputBox(screen, 150, 200, 500, 60, black)

    # Draw all fonts
    title_text = title_font.render("Midpoint circle visualization", True, black)

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    screen.blit(title_text, (120, 100))
    radius_input_field_rect.draw()

    # Event loop
    while True:
        # For quiting
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_BACKSPACE:
                    radius_input_field_rect.clear()

                if event.unicode in string.digits:
                    radius_input_field_rect.update(event.unicode)

            pygame_widgets.update(event)
            pygame.display.update()


if __name__ == "__main__":
    main()
