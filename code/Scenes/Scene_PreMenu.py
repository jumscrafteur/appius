import pygame
from Button import Button_img
from Scene import Scene
from .Scene_ids import SCENE_PREMENU_ID, SCENE_MENU_ID


def preMenuCreate(self):
    self.buttons['btn1'] = Button_img(self.game.screen_width/2, self.game.screen_height/2,
                                      lambda: self.game.switchScene(SCENE_MENU_ID), "/Users/jumscrafteur/workspace/cours/STI3A/python/Projet-Appius/appius/assets/C3title_00001.png")


def preMenuRun(self):
    pygame.time.Clock().tick(60)

    self.buttons['btn1'].show(self.game.screen)

    pygame.display.flip()


SCENE = Scene(SCENE_PREMENU_ID, 'preMenu',
              createFunc=preMenuCreate, runFunc=preMenuRun)
