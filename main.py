#!/usr/bin/python3

import pygame
import sys
import utils
import string
import classes

from pygame_widgets.button import Button
import pygame_widgets

def hollow_button_func(button, value):
    filled = value

def start_button_func(radius, surface, bg, start_button, circle_type, hollow_button, filled_button):
    start_button.hide()
    hollow_button.hide()
    filled_button.hide()
    try:
        if circle_type == None:
            circle_type = True

        try:
            radius = int(radius.string_of_keys)
        except ValueError:
            radius = 200

        surface.blit(bg, (0, 0))
        print(radius)
        if circle_type:
            list_of_filled_rect_coords = utils.fill_circle(WIDTH, HEIGHT, radius)
            for el in list_of_filled_rect_coords:
                pygame.draw.rect(surface, (0, 0, 0), pygame.Rect(el[0], el[1], 1, 1))
        if not circle_type:
            list_of_rect_coords = utils.better_midpoint_circle_draw(
                WIDTH, HEIGHT, radius
            )
            for el in list_of_rect_coords:
                pygame.draw.rect(surface, (0, 0, 0), pygame.Rect(el[0], el[1], 1, 1))
    except Exception as e:
        print("Exception: ", e)


def main() -> None:

    pygame.init()

    def assign_value_to_filled(value):
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
        onClick=lambda: start_button_func(
            radius_input_field_rect, screen, background, start_button, filled, hollow_circle_button, filled_circle_button
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
        onClick=lambda: assign_value_to_filled(True),
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
        onClick=lambda: assign_value_to_filled(False),
    )
    # hollow_circle_button = pygame.Rect(450, 300, 200, 100)
    radius_input_field_rect = classes.InputBox(screen, 150, 200, 500, 60, BLACK)

    # Draw all fonts
    title_text = TITLE_FONT.render("Midpoint circle visualization", True, BLACK)
    # hollow_button_text = BUTTON_FONT.render("HOLLOW CIRCLE", True, WHITE)

    # Blit everything to the screen
    screen.blit(background, (0, 0))

    # pygame.draw.rect(screen, GRAY, hollow_circle_button)

    screen.blit(title_text, (120, 100))
    # screen.blit(hollow_button_text, (450 + 2, 300 + 40))
    radius_input_field_rect.draw()

    # Event loop
    while True:
        # For quiting
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_coords = pygame.mouse.get_pos()

                """
                if utils.is_over(
                    filled_circle_button, (mouse_coords[0], mouse_coords[1])
                ):
                    filled = True

                # Over hollow circle button
                if utils.is_over(
                    hollow_circle_button, (mouse_coords[0], mouse_coords[1])
                ):
                    filled = False
                """

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_BACKSPACE:
                    radius_input_field_rect.clear()

                if event.unicode in string.digits:
                    radius_input_field_rect.update(event.unicode)

        pygame.display.update()
        pygame_widgets.update(event)


if __name__ == "__main__":
    main()
