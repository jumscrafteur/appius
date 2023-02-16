import pygame
from Const import SceneIds
from Scene import Scene


def create(self):
    pass


def run(self):
    self.game.screen.fill((46, 204, 113))


def event(self, event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            self.game.switchScene(SceneIds.Scene1)


SCENE = Scene(SceneIds.Scene2, createFunc=create, runFunc=run, handleEventsFunc=event)
