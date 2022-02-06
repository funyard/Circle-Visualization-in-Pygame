#!python

import pygame
import sys
import utils
import string
import classes


def main() -> None:

    pygame.init()

    # VARS
    WIDTH, HEIGHT = 800, 600
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 240)
    GRAY = (15, 15, 15)
    TITLE_FONT = pygame.font.Font(None, 60)
    BUTTON_FONT = pygame.font.Font(None, 34)

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
    radius_input_field_rect = classes.InputBox(screen, 150, 200, 500, 60, BLACK)

    # Draw all fonts
    title_text = TITLE_FONT.render("Midpoint circle visualization", True, BLACK)
    start_button_text = BUTTON_FONT.render("START", True, WHITE)
    filled_button_text = BUTTON_FONT.render("FILLED CIRCLE", True, WHITE)
    hollow_button_text = BUTTON_FONT.render("HOLLOW CIRCLE", True, WHITE)

    # Blit everything to the screen
    screen.blit(background, (0, 0))

    pygame.draw.rect(screen, BLUE, start_button)
    pygame.draw.rect(screen, GRAY, filled_circle_button)
    pygame.draw.rect(screen, GRAY, hollow_circle_button)

    screen.blit(title_text, (120, 100))
    screen.blit(start_button_text, ((400 - 200 / 2) + 65, 440 + 40))
    screen.blit(hollow_button_text, (450 + 2, 300 + 40))
    screen.blit(filled_button_text, (150 + 13, 300 + 40))
    radius_input_field_rect.draw()

    # Event loop
    while True:
        # For quiting
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_coords = pygame.mouse.get_pos()

                # Over start button
                if utils.is_over(start_button, (mouse_coords[0], mouse_coords[1])):
                    try:
                        if filled == None:
                            filled = True

                        try:
                            radius = int(radius_input_field_rect.string_of_keys)
                        except ValueError:
                            radius = 200

                        screen.blit(background, (0, 0))
                        print(radius)
                        if filled:
                            list_of_filled_rect_coords = utils.fill_circle(
                                WIDTH, HEIGHT, radius
                            )
                            for el in list_of_filled_rect_coords:
                                pygame.draw.rect(
                                    screen, BLACK, pygame.Rect(el[0], el[1], 1, 1)
                                )
                        if not filled:
                            list_of_rect_coords = utils.better_midpoint_circle_draw(
                                WIDTH, HEIGHT, radius
                            )
                            for el in list_of_rect_coords:
                                pygame.draw.rect(
                                    screen, BLACK, pygame.Rect(el[0], el[1], 1, 1)
                                )
                    except Exception as e:
                        print("Exception: ", e)

                # Over filled circle button
                if utils.is_over(
                    filled_circle_button, (mouse_coords[0], mouse_coords[1])
                ):
                    filled = True

                # Over hollow circle button
                if utils.is_over(
                    hollow_circle_button, (mouse_coords[0], mouse_coords[1])
                ):
                    filled = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_BACKSPACE:
                    radius_input_field_rect.clear()

                if event.unicode in string.digits:
                    radius_input_field_rect.update(event.unicode)

        pygame.display.update()


if __name__ == "__main__":
    main()
