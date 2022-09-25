import pygame
from math import ceil

class Background:
    def __init__(self, SCREEN, background_image):
        self.scroll = 0
        self.SCREEN = SCREEN
        self.background_image = background_image
        self.bg_width = self.background_image.get_width()
        self.game_speed = 5

    def scroll_background(self):
        tiles = ceil(self.SCREEN.get_width() / self.bg_width) + 1
        for i in range(tiles):
            self.SCREEN.blit(self.background_image, (i*self.bg_width+self.scroll, 0))
        self.scroll -= self.game_speed
        if abs(self.scroll) > self.bg_width:
                self.scroll = 0