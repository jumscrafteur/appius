import os
from typing import Annotated, Callable, Dict, List, Tuple, TypedDict

import pygame
from Const import ASSET_PATH
from LayoutManager import drawCenter

assets = {}


def load(name: str, path: str):
    assets[name] = pygame.image.load(os.path.join(ASSET_PATH, path))


def get(name: str) -> pygame.Surface:
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


FONT_LETTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!\"%*()-+=:;'?\\/,._äáàâëéèêïíìîöóòôüúùûçñæßÄÉÜÑÆŒœÁÂÀÊÈÍÎÌÓÔÒÖÚÛÙ¡¿^°ÅØåø "

FontType = Annotated[Tuple[pygame.Surface], len(FONT_LETTERS)]


class FONTS:
    base: FontType = tuple(
        pygame.image.load(os.path.join(ASSET_PATH, f"fonts/{i:05}.png"))
        for i in range(1, 1 + len(FONT_LETTERS))
    )


def getTextAsSurface(
    font: Annotated[Tuple[pygame.Surface], 3], text: str, spacing: int = 2
) -> pygame.Surface:
    textTotalSize = [0, 0]
    fontDict: Dict[str, pygame.Surface] = {
        c: fontTile for c, fontTile in zip(FONT_LETTERS, font)
    }
    spaceSize = 5

    for c in text:
        if c == " ":
            textTotalSize[0] += spaceSize
            continue

        textTotalSize[0] += fontDict[c].get_size()[0] + spacing
        textTotalSize[1] = max(textTotalSize[1], fontDict[c].get_size()[1])

    textSurface = pygame.Surface(textTotalSize)
    textSurface.fill((0, 0, 0, 0))

    offset = 0
    for c in text:
        if c == " ":
            offset += spaceSize
            continue
        sprite = fontDict[c]
        textSurface.blit(sprite, (offset, 0))
        offset += sprite.get_size()[0] + spacing

    return textSurface.convert_alpha()


class ButtonSchema(TypedDict):
    tileSelector: Callable[[Tuple[int, int], Tuple[int, int]], Tuple[int, int]]
    tileSize: Tuple[int, int]
    neutral: List[List[pygame.Surface]]
    over: List[List[pygame.Surface]]
    font: FontType


class BUTTON_TYPES:
    PRIMARY: ButtonSchema = {
        "tileSelector": lambda pos, buttonSize: (0, 0)
        if pos[0] == 0
        else (2, 0)
        if pos[0] == buttonSize[0] - 1
        else (1, 0),
        "tileSize": (16, 25),
        "neutral": [
            [
                pygame.image.load(os.path.join(ASSET_PATH, f"paneling/000{i}.png"))
                for i in range(22, 25)
            ]
        ],
        "over": [
            [
                pygame.image.load(os.path.join(ASSET_PATH, f"paneling/000{i}.png"))
                for i in range(25, 28)
            ]
        ],
        "font": FONTS.base,
    }


class Button:
    def __init__(
        self,
        neutralSurface: pygame.Surface,
        overSurface: pygame.Surface,
        pos: Tuple[int, int],
        clickEvent: Callable,
    ) -> None:
        self.neutralSurface = neutralSurface
        self.overSurface = overSurface

        pos = tuple(pos[i] - overSurface.get_size()[i] // 2 for i in range(2))

        self.rect = pygame.Rect(
            pos,
            overSurface.get_size(),
        )

        self.overed = False
        self.position = pos

        self.clickEvent = clickEvent

    def render(self, destSurface: pygame.Surface):
        destSurface.blit(
            self.overSurface if self.overed else self.neutralSurface, self.position
        )

    def checkOver(self):
        self.overed = self.rect.collidepoint(pygame.mouse.get_pos())

    def checkClick(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.clickEvent()


class ButtonText(Button):
    def __init__(
        self,
        theme: ButtonSchema,
        pos: Tuple[int, int],
        size: Tuple[int, int],
        text: str,
        clickEvent: Callable,
    ) -> None:
        neutralSurface = pygame.Surface(
            (theme["tileSize"][0] * size[0], theme["tileSize"][1] * size[1])
        )
        overSurface = pygame.Surface(
            (theme["tileSize"][0] * size[0], theme["tileSize"][1] * size[1])
        )

        for x in range(size[0]):
            for y in range(size[1]):
                tileIndex = theme["tileSelector"]((x, y), size)
                neutralSurface.blit(
                    theme["neutral"][tileIndex[1]][tileIndex[0]],
                    (x * theme["tileSize"][0], y * theme["tileSize"][1]),
                )
                overSurface.blit(
                    theme["over"][tileIndex[1]][tileIndex[0]],
                    (x * theme["tileSize"][0], y * theme["tileSize"][1]),
                )

        textSurface = getTextAsSurface(FONTS.base, text)

        drawCenter(neutralSurface, textSurface)
        drawCenter(overSurface, textSurface)

        super(ButtonText, self).__init__(neutralSurface, overSurface, pos, clickEvent)


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
