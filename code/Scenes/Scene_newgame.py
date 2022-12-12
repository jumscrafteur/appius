from Scene import *
import pygame
from Button import *
from Inputbox import InputBox
from const import *
from .Scene_ids import *


def SceneNewGameCreate(self):
    self.images["fond"] = pygame.image.load(
        "assets/01b_00001.png").convert()

    self.box["inputbox"] = InputBox(
        self.game.screen_width/2, self.game.screen_height/2, 600, 30,  pygame.event.post(pygame.event.Event(
            event_types["LaunchGame"], {"name": 1})))

    self.buttons["btn1"] = Button_text(self.game.screen_width/2-150, self.game.screen_height /
                                       2+50, 100, 100, lambda: self.game.switchScene(SCENE_MENU_ID), "Back to Menu")
    self.buttons["btn2"] = Button_text(self.game.screen_width/2+150, self.game.screen_height /
                                       2+50, 100, 100, lambda: pygame.event.post(pygame.event.Event(
                                           event_types["LaunchGame"], {"name": 1})), "Go to Game")


def SceneNewGameRun(self):

    pygame.time.Clock().tick(60)
    self.game.screen.blit(pygame.transform.scale(
        self.images["fond"], (self.game.screen_width, self.game.screen_height)), (0, 0))

    for key in self.box.keys():
        self.box[key].show(self.game.screen)

    for key in self.buttons.keys():
        self.buttons[key].show(self.game.screen, False)

    pygame.display.flip()


def SceneNewGamehandleEventsFunc(self, event):
    print("ok1")
    if event.type == event_types["LaunchGame"]:
        print("ok2")
        self.game.save = self.box["inputbox"].text
        self.game.switchScene(SCENE_GAME_ID)


SCENE = Scene(SCENE_NEWGAME_ID, 'Scene_newgame', createFunc=SceneNewGameCreate,
              runFunc=SceneNewGameRun, handleEventsFunc=SceneNewGamehandleEventsFunc)
