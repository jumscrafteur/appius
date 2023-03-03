import os
from typing import Callable, List, Tuple, TypedDict

import pygame
from Const import ASSET_PATH
from LayoutManager import drawCenter

from Assets.Font import FONTS, FontType, getTextAsSurface


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
        visible: bool = True,
    ) -> None:
        self.neutralSurface = neutralSurface
        self.overSurface = overSurface

        pos = tuple(pos[i] - overSurface.get_size()[i] // 2 for i in range(2))

        self.rect = pygame.Rect(
            pos,
            overSurface.get_size(),
        )

        self.overed = False
        self.relativePosition = pos

        self.absolutePosition = pos

        self.clickEvent = clickEvent

        self.visible = visible

    def render(self, destSurface: pygame.Surface):
        if self.visible:
            destSurface.blit(
                self.overSurface if self.overed else self.neutralSurface,
                self.relativePosition,
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

        textSurface = getTextAsSurface(theme["font"], text)

        drawCenter(neutralSurface, textSurface)
        drawCenter(overSurface, textSurface)

        super(ButtonText, self).__init__(neutralSurface, overSurface, pos, clickEvent)
