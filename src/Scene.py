from typing import Callable, Optional

import pygame
from Game import Game


class Scene:
    def __init__(
        self,
        id: int,
        createFunc=None,
        runFunc=None,
        destroyFunc=None,
        handleEventsFunc=None,
    ):
        self.id: int = id
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
            if event.type == pygame.USEREVENT:
                event.action()

            self.handleEventsFunc(self, event)

    def destroy(self):
        self.destroyFunc(self)