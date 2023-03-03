from typing import Callable, List, Optional

import pygame
from Const import CustomEvent, SceneIds
from Game import Game

from Assets import Button, Panel


class Scene:
    def __init__(
        self,
        id: SceneIds,
        createFunc=None,
        runFunc=None,
        destroyFunc=None,
        handleEventsFunc=None,
    ):
        self.id: SceneIds = id
        self.game: Optional[Game] = None

        self.createFunc: Callable[[Scene], None] = (
            createFunc if createFunc else lambda scene: None
        )

        self.runFunc: Callable[[Scene], None] = (
            runFunc if runFunc else lambda scene: None
        )

        self.destroyFunc: Callable[[Scene], None] = (
            destroyFunc if destroyFunc else lambda scene: None
        )

        self.handleEventsFunc: Callable[[Scene, pygame.event.Event], None] = (
            handleEventsFunc if handleEventsFunc else lambda scene, event: None
        )

        self.buttons: List[Button] = []
        self.panels: List[Panel] = []

    def create(self, game):
        self.game = game
        self.createFunc(self)
        return

    def run(self):
        self.runFunc(self)

    def handleEvents(self):
        assert self.game

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.end()
            if event.type == CustomEvent.SwitchScene:
                self.game.switchScene(event.id)

            self.handleEventsFunc(self, event)

    def destroy(self):
        assert self.game

        self.game.screen.fill((0, 0, 0))
        self.destroyFunc(self)
