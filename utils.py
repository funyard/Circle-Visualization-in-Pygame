from typing import List
import pygame


def fill_circle(x, y, r) -> List[List]:
    """
    Function which loops through every pixel in pygame window. If the pixel is inside the circle, it adds the pixel's coordinates to the list of pixels, which is returned.
    """

    width = x
    height = y
    list_of_coords = []

    for x in range(width):
        for y in range(height):
            if (x - width / 2) ** 2 + (y - height / 2) ** 2 <= r**2:
                list_of_coords.append([x, y])

    return list_of_coords


# MY OWN IMPLEMENTATION -> inefficient
def midpoint_circle_draw(x, y, r) -> List[List]:
    """
    Function loops through every pixel in pygame window. If the pixel's coordinates squared and added together equal 1, it is added to the list of pixels, which is returned.
    NOTE: Because the added coordinates are usualy not exactly 0, there is also a list, which contains the deviation.
    """
    width = x
    height = y
    list_of_coords = []
    max_deviancy = [*range(r**2 - 175, r**2 + 175)]

    for x in range(width):
        for y in range(height):
            if (x - width / 2) ** 2 + (y - height / 2) ** 2 in max_deviancy:
                list_of_coords.append([x, y])

    return list_of_coords


# CREDIT: https://www.geeksforgeeks.org/mid-point-circle-drawing-algorithm/
def better_midpoint_circle_draw(x_centre, y_centre, r):
    x_centre = x_centre / 2
    y_centre = y_centre / 2
    x = r
    y = 0
    list_of_points = []

    # Printing the initial point the
    # axes after translation

    # When radius is zero only a single
    # point be printed
    if r > 0:

        list_of_points.append((x + x_centre, -y + y_centre))
        list_of_points.append((y + x_centre, x + y_centre))
        list_of_points.append((-y + x_centre, x + y_centre))

    # Initialising the value of P
    P = 1 - r

    while x > y:

        y += 1

        # Mid-point inside or on the perimeter
        if P <= 0:
            P = P + 2 * y + 1

        # Mid-point outside the perimeter
        else:
            x -= 1
            P = P + 2 * y - 2 * x + 1

        # All the perimeter points have
        # already been printed
        if x < y:
            break

        # Printing the generated point its reflection
        # in the other octants after translation

        list_of_points.append((x + x_centre, y + y_centre))
        list_of_points.append((-x + x_centre, y + y_centre))
        list_of_points.append((x + x_centre, -y + y_centre))
        list_of_points.append((-x + x_centre, -y + y_centre))

        # If the generated point on the line x = y then
        # the perimeter points have already been printed
        if x != y:

            list_of_points.append((y + x_centre, x + y_centre))
            list_of_points.append((-y + x_centre, x + y_centre))
            list_of_points.append((y + x_centre, -x + y_centre))
            list_of_points.append((-y + x_centre, -x + y_centre))

    return list_of_points


def is_over(rect, pos):
    """
    function takes a tuple of (x, y) coords and a pygame.Rect object
    returns True if the given rect overlaps the given coords
    else it returns False
    """
    return True if rect.collidepoint(pos[0], pos[1]) else False


def start_button_func(
    radius, surface, bg, start_button, circle_type, hollow_button, filled_button
):
    WIDTH, HEIGHT = 800, 600
    start_button.hide()
    hollow_button.hide()
    filled_button.hide()
    try:
        try:
            if circle_type == None:
                circle_type = False
        except NameError:
            circle_type = False

        try:
            radius = int(radius.string_of_keys)
        except ValueError:
            radius = 200

        surface.blit(bg, (0, 0))
        print(radius)
        if circle_type:
            list_of_filled_rect_coords = fill_circle(WIDTH, HEIGHT, radius)
            for el in list_of_filled_rect_coords:
                pygame.draw.rect(surface, (0, 0, 0), pygame.Rect(el[0], el[1], 1, 1))
        if not circle_type:
            list_of_rect_coords = better_midpoint_circle_draw(WIDTH, HEIGHT, radius)
            for el in list_of_rect_coords:
                pygame.draw.rect(surface, (0, 0, 0), pygame.Rect(el[0], el[1], 1, 1))
    except Exception as e:
        print("Exception: ", e)
