import pygame
from pygame.locals import *
import os


class App:
    def __init__(self):
        self.running = True
        self.size = (800, 600)

        # create window
        self.window = pygame.display.set_mode(
            self.size, pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.RESIZABLE)

        # create map
        # currentdir = os.path.dirname(os.path.realpath(__file__))
        # imagedir = currentdir+'europe.png'
        self.map = pygame.image.load('Testing/europe.png')
        self.maprect = self.map.get_rect(center=self.window.get_rect().center)
        self.blitmap()

        # create window
        pygame.display.flip()

    def blitmap(self):
        self.mapsurface = pygame.transform.smoothscale(
            self.map, self.maprect.size)
        self.window.fill(0)
        self.window.blit(self.mapsurface, self.maprect)

    def on_init(self):
        self.country = Country()

    def on_cleanup(self):
        pygame.quit()

    def check_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False

        elif event.type == pygame.VIDEORESIZE:
            self.window = pygame.display.set_mode(
                event.dict['size'], pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.RESIZABLE)
            self.blitmap()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4 or event.button == 5:
                zoom = 2 if event.button == 4 else 0.5
                mx, my = event.pos
                left = mx + (self.maprect.left - mx) * zoom
                right = mx + (self.maprect.right - mx) * zoom
                top = my + (self.maprect.top - my) * zoom
                bottom = my + (self.maprect.bottom - my) * zoom
                self.maprect = pygame.Rect(left, top, right-left, bottom-top)
                self.blitmap()

        pygame.display.update()

    def on_execute(self):
        while self.running == True:
            for event in pygame.event.get():
                self.check_event(event)
        self.on_cleanup()


class Country(App):
    def __init__(self):
        super().__init__()


start = App()
start.on_init()
start.on_execute()
