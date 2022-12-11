from Scene import *
import pygame
from Button import *
from const import *
from .Scene_ids import SCENE_MENU_ID


def SceneMenuCreate(self):
    self.images["fond"] = pygame.image.load(
        "assets/0_fired_00001.png").convert()

    self.buttons["button_start"] = Button_text(
        self.game.screen_width/2, self.game.screen_height/2 - 225, 200, 100, lambda: print("ok"), "Start Game")
    self.buttons["button_load"] = Button_text(
        self.game.screen_width/2, self.game.screen_height/2 - 75, 200, 100, lambda: print("ok"), "Load a Game")
    self.buttons["button_options"] = Button_text(
        self.game.screen_width/2, self.game.screen_height/2 + 75, 200, 100, lambda: print("ok"), "Options")
    self.buttons["button_exit"] = Button_text(
        self.game.screen_width/2, self.game.screen_height/2 + 225, 200, 100, self.game.end, "Exit Game")


def SceneMenuRun(self):

    pygame.time.Clock().tick(60)
    self.game.screen.blit(pygame.transform.scale(
        self.images["fond"], (self.game.screen_width, self.game.screen_height)), (0, 0))

    for key in self.buttons.keys():
        self.buttons[key].show(self.game.screen)

    pygame.display.flip()


SCENE = Scene(SCENE_MENU_ID, 'Scene_Menu', createFunc=SceneMenuCreate,
              runFunc=SceneMenuRun)
