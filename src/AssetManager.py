import os
from typing import List

import pygame
from Const import ASSET_PATH

assets = {}


def load(name: str, path: str):
    assets[name] = pygame.image.load(os.path.join(ASSET_PATH, path))


def get(name: str):
    return assets[name]


def loadPuzzleAsset(
    name: str, pathList: List[str], size: int, horizontalCount: int, verticalCount: int
):
    asset = pygame.Surface((size * horizontalCount, size * verticalCount))

    for x in range(horizontalCount):
        for y in range(verticalCount):
            tileImage = pygame.image.load(
                os.path.join(ASSET_PATH, pathList[x + y * horizontalCount])
            )
            asset.blit(tileImage, (x * size, y * size))

    assets[name] = asset


PANEL_ASSETS_MAP = {
    "corner_upper_left": pygame.image.load(
        os.path.join(ASSET_PATH, "paneling/00335.png")
    ),
    "corner_upper_right": pygame.image.load(
        os.path.join(ASSET_PATH, "paneling/00346.png")
    ),
    "corner_lower_left": pygame.image.load(
        os.path.join(ASSET_PATH, "paneling/00467.png")
    ),
    "corner_lower_right": pygame.image.load(
        os.path.join(ASSET_PATH, "paneling/00478.png")
    ),
    "border_left": [
        pygame.image.load(os.path.join(ASSET_PATH, f"paneling/00{i}.png"))
        for i in range(347, 456, 12)
    ],
    "border_right": [
        pygame.image.load(os.path.join(ASSET_PATH, f"paneling/00{i}.png"))
        for i in range(358, 467, 12)
    ],
    "border_top": [
        pygame.image.load(os.path.join(ASSET_PATH, f"paneling/00{i}.png"))
        for i in range(336, 446)
    ],
    "border_bottom": [
        pygame.image.load(os.path.join(ASSET_PATH, f"paneling/00{i}.png"))
        for i in range(468, 478)
    ],
    "filler": [
        [
            pygame.image.load(os.path.join(ASSET_PATH, f"paneling/00{i}.png"))
            for i in range(rowOffset, rowOffset + 10)
        ]
        for rowOffset in range(348, 466, 12)
    ],
}


def createPanel(name: str, horizontalCount: int, verticalCount: int):
    # si (0,0):
    #     coins haut gauche
    # si (horizontalCount - 1,0):
    #     coins haut droite
    # si (0,verticalCount - 1):
    #     coins bas gauche
    # si (horizontalCount - 1,verticalCount - 1):
    #     coins bas droite

    # si (0, y):
    #     bordure_gauche y % 10
    # si (verticalCount - 1 , y):
    #     bordure_droite (y-1) % 10
    # si (x, 0):
    #     bordure_haut (x-1) % 10
    # si (x, horizontalCount - 1):
    #     bordure_bas (x-1) % 10
    # si (x, y):
    #     filler (y-1) % 10, (x-1) % 10

    PANEL_TILE_SIZE = 16

    asset = pygame.Surface(
        (horizontalCount * PANEL_TILE_SIZE, verticalCount * PANEL_TILE_SIZE)
    )

    for x in range(horizontalCount):
        for y in range(verticalCount):
            pos = (x, y)
            if pos == (0, 0):
                tileImage = PANEL_ASSETS_MAP["corner_upper_left"]
            elif pos == (horizontalCount - 1, 0):
                tileImage = PANEL_ASSETS_MAP["corner_upper_right"]
            elif pos == (0, verticalCount - 1):
                tileImage = PANEL_ASSETS_MAP["corner_lower_left"]
            elif pos == (horizontalCount - 1, verticalCount - 1):
                tileImage = PANEL_ASSETS_MAP["corner_lower_right"]
            elif x == 0:
                tileImage = PANEL_ASSETS_MAP["border_left"][(x - 1) % 10]
            elif x == horizontalCount - 1:
                tileImage = PANEL_ASSETS_MAP["border_right"][(x - 1) % 10]
            elif y == 0:
                tileImage = PANEL_ASSETS_MAP["border_top"][(y - 1) % 10]
            elif y == verticalCount - 1:
                tileImage = PANEL_ASSETS_MAP["border_bottom"][(y - 1) % 10]
            else:
                tileImage = PANEL_ASSETS_MAP["filler"][(y - 1) % 10][(x - 1) % 10]

            asset.blit(tileImage, (x * PANEL_TILE_SIZE, y * PANEL_TILE_SIZE))

            pass

    assets[name] = asset
