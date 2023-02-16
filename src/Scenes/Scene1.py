import pygame
from Const import SceneIds
from Scene import Scene


def create(self):
    pass


def run(self):
    self.game.screen.fill((231, 76, 60))


def event(self, event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            self.game.switchScene(SceneIds.Scene2)


SCENE = Scene(SceneIds.Scene1, createFunc=create, runFunc=run, handleEventsFunc=event)
