import AssetManager
import pygame
from Const import SceneIds
from LayoutManager import drawCenter
from Scene import Scene


def create(self: Scene):
    assert self.game

    AssetManager.load("menu_background", "0/fired/00001.png")
    AssetManager.transform(
        "menu_background", lambda asset: pygame.transform.scale_by(asset, 1.5)
    )
    AssetManager.createPanel("panel", 20, 22)

    testBtn = AssetManager.ButtonText(
        AssetManager.BUTTON_TYPES.PRIMARY,
        tuple(v // 2 for v in self.game.screen.get_size()),
        (7, 1),
        "Salut",
        lambda: print("salut"),
    )

    self.buttons.append(testBtn)

    drawCenter(self.game.screen, AssetManager.get("menu_background"))
    drawCenter(self.game.screen, AssetManager.get("panel"))


def run(self: Scene):
    assert self.game

    for button in self.buttons:
        button.render(self.game.screen)

    pass


def event(self: Scene, event: pygame.event.Event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        for button in self.buttons:
            button.checkClick()
    elif event.type == pygame.MOUSEMOTION:
        for button in self.buttons:
            button.checkOver()


SCENE = Scene(SceneIds.Menu, createFunc=create, runFunc=run, handleEventsFunc=event)
