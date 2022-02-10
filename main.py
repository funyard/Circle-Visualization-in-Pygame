#!python3

import pygame
import sys
import utils
import string
import classes

from pygame_widgets.button import Button
import pygame_widgets


def main() -> None:

    pygame.init()

    def set_circle_type(value):
        filled = value

    # VARS
    global WIDTH, HEIGHT, filled
    filled = None
    WIDTH, HEIGHT = 800, 600
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 240)
    GRAY = (15, 15, 15)
    TITLE_FONT = pygame.font.Font(None, 60)

    # Initialise screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Midpoint circle visualization")

    # Fill background
    background = pygame.Surface(screen.get_size())
    background.fill(WHITE)

    # Create main menu
    start_button = Button(
        screen,
        400 - 200 / 2,
        440,
        200,
        100,
        text="START",
        textColour=WHITE,
        fontsize=34,
        margin=20,
        inactiveColour=BLUE,
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
        textColour=WHITE,
        fontsize=34,
        margin=20,
        inactiveColour=GRAY,
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
        textColour=WHITE,
        fontsize=34,
        margin=20,
        inactiveColour=GRAY,
        pressedColour=(20, 20, 90),
        radius=4,
        onClick=lambda: set_circle_type(False),
    )
    radius_input_field_rect = classes.InputBox(screen, 150, 200, 500, 60, BLACK)

    # Draw all fonts
    title_text = TITLE_FONT.render("Midpoint circle visualization", True, BLACK)

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

        pygame.display.update()
        pygame_widgets.update(event)


if __name__ == "__main__":
    main()
