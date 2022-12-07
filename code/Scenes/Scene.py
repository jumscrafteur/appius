from __future__ import annotations
from time import sleep
from typing import Callable, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from Game import Game


class Scene():
    def __init__(self, id: int, name: str,
                 createFunc: Callable[['Scene'], None] = lambda scene: None,
                 runFunc: Callable[['Scene'], None] = lambda scene: None,
                 destroyFunc: Callable[['Scene'], None] = lambda scene: None
                 ) -> None:
        self.name = name
        self.id = id
        self.game: Optional[Game] = None
        self.createFunc = createFunc
        self.runFunc = runFunc
        self.destroyFunc = destroyFunc

    def create(self, game: Game) -> None:
        self.game = game
        self.createFunc(self)
        return

    def run(self) -> None:
        self.runFunc(self)

    def destroy(self) -> None:
        self.destroyFunc(self)
