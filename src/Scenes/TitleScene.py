import AssetManager
import pygame
from Const import SceneIds
from LayoutManager import drawCenter
from Scene import Scene


def create(self: Scene):
    AssetManager.load("title_screen", "C3title/00001.png")


def run(self: Scene):
    assert self.game is not None

    drawCenter(self.game.screen, AssetManager.get("title_screen"))


def event(self: Scene, event):
    assert self.game is not None

    if event.type in [pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN]:
        self.game.switchScene(SceneIds.Menu)


SCENE = Scene(SceneIds.Title, createFunc=create, runFunc=run, handleEventsFunc=event)
