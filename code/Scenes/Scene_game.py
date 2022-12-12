from Scene import Scene
from .Scene_ids import SCENE_GAME_ID


def SceneGameCreate(self):
    pass


def SceneGameRun(self):
    pass


SCENE = Scene(SCENE_GAME_ID, 'Scene_Menu', createFunc=SceneGameCreate,
              runFunc=SceneGameRun)
