import pygame
from Button import Button


def preMenuCreate(self):
    self.images = {}
    self.buttons = {}

    self.image['waitingScreen'] = pygame.image.load("C3title_00001.png")
    self.image['fond'] = pygame.image.load("0_fired_00001.png").convert()

    self.buttons['btn1'] = Button(
        self.game.screen_height/4, self.game.screen_width/2, 200, 100, "paneling_00231.png", "Load game")
