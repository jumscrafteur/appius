import pygame
from Button import Button_img
from Scene import Scene


def preMenuCreate(self):
    self.buttons = {}

    self.buttons['btn1'] = Button_img(self.game.screen_width/2, self.game.screen_height/2,
                                      lambda: print("ok"), "/Users/jumscrafteur/workspace/cours/STI3A/python/Projet-Appius/appius/assets/C3title_00001.png")


def preMenuRun(self):
    pygame.time.Clock().tick(60)

    self.buttons['btn1'].show(self.game.screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.buttons['btn1'].MouseonButton(event.pos)
        if event.type == pygame.USEREVENT:
            event.action()

    pygame.display.flip()


SCENE = Scene(0, 'preMenu', createFunc=preMenuCreate, runFunc=preMenuRun)
