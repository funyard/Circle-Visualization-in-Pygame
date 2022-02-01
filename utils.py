from typing import List


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


def midpoint_circle_draw(x, y, r) -> List[List]:
    """
    Function loops through every pixel in pygame window. If the pixel's coordinates squared and added together equal 1, it is added to the list of pixels, which is returned.
    NOTE: Because the coordinates are usualy not exactly 0, there is also a list, which contains the deviation.
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
