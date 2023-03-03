import os
from typing import Callable, List, Tuple

import pygame
from Const import ASSET_PATH

assets = {}


def load(name: str, path: str):
    assets[name] = pygame.image.load(os.path.join(ASSET_PATH, path))


def add(name: str, asset: pygame.Surface):
    assets[name] = asset


def getAsset(name: str) -> pygame.Surface:
    return assets[name]


def transform(name: str, transformation: Callable[[pygame.Surface], pygame.Surface]):
    assets[name] = transformation(assets[name])
    pass


def loadPuzzleAsset(
    name: str,
    pathList: List[str],
    size: Tuple[int, int],
    horizontalCount: int,
    verticalCount: int,
):
    asset = pygame.Surface((size[0] * horizontalCount, size[1] * verticalCount))

    for x in range(horizontalCount):
        for y in range(verticalCount):
            tileImage = pygame.image.load(
                os.path.join(ASSET_PATH, pathList[x + y * horizontalCount])
            )
            asset.blit(tileImage, (x * size[0], y * size[1]))

    assets[name] = asset
