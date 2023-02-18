import AssetManager
import pygame
from Const import SceneIds
from LayoutManager import drawCenter
from Scene import Scene


def create(self):
    AssetManager.load("menu_background", "0/fired/00001.png")
    AssetManager.transform(
        "menu_background", lambda asset: pygame.transform.scale_by(asset, 1.5)
    )
    AssetManager.createPanel("panel", 20, 22)

    testBtn = AssetManager.ButtonText(
        AssetManager.BUTTON_TYPES.PRIMARY, (7, 1), "salut"
    )

    drawCenter(self.game.screen, AssetManager.get("menu_background"))
    drawCenter(self.game.screen, AssetManager.get("panel"))
    drawCenter(self.game.screen, testBtn.neutralSurface)


def run(self):
    pass


def event(self, event):
    pass


SCENE = Scene(SceneIds.Menu, createFunc=create, runFunc=run, handleEventsFunc=event)
