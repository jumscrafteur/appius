import os
from typing import Annotated, Dict, Tuple

import pygame
from Const import ASSET_PATH

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
    textSurface.fill((255, 255, 255))
    textSurface.set_colorkey((255, 255, 255))

    offset = 0
    for c in text:
        if c == " ":
            offset += spaceSize
            continue
        sprite = fontDict[c]
        textSurface.blit(sprite, (offset, 0))
        offset += sprite.get_size()[0] + spacing

    return textSurface
