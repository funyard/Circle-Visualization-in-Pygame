import pygame
import string


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
