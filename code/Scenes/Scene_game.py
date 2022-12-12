from Scene import Scene
from .Scene_ids import SCENE_GAME_ID
from map_init.game.map import MapGame
import pygame


def SceneGameCreate(self):
    self.game.map = MapGame(self.game.screen, pygame.time.Clock())


def SceneGameRun(self):
    self.game.map.run()


def SceneGameHandleEvents(self, event):
    pass


SCENE = Scene(SCENE_GAME_ID, 'Scene_Menu', createFunc=SceneGameCreate,
              runFunc=SceneGameRun)
