from typing import List


def fill_circle(x, y, r) -> List[List]:
    width = x
    height = y
    list_of_coords = []

    for x in range(width):
        for y in range(height):
            if (x - width / 2) ** 2 + (y - height / 2) ** 2 <= r**2:
                list_of_coords.append([x, y])

    return list_of_coords


def midpoint_circle_draw(x, y, r) -> List[List]:
    width = x
    height = y
    list_of_coords = []
    max_deviancy = [*range(r**2 - 175, r**2 + 175)]

    for x in range(width):
        for y in range(height):
            if (x - width / 2) ** 2 + (y - height / 2) ** 2 in max_deviancy:
                list_of_coords.append([x, y])

    return list_of_coords


