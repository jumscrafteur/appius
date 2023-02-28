import pygame


def drawCenter(destSurface: pygame.surface.Surface, srcSurface: pygame.surface.Surface):
    destSurfaceSize = destSurface.get_size()
    srcSurfaceSize = srcSurface.get_size()

    centerPosition = (
        destSurfaceSize[0] / 2 - srcSurfaceSize[0] / 2,
        destSurfaceSize[1] / 2 - srcSurfaceSize[1] / 2,
    )

    destSurface.blit(srcSurface, centerPosition)


def GenerateGridLayout(x, y, columnNumber, rowNumber, gapX, gapY, sizeX, sizeY):
    initialOffsetX = -(columnNumber - 1) * (gapX + sizeX) / 2
    initialOffsetY = -(rowNumber - 1) * (gapY + sizeY) / 2

    for c in range(columnNumber):
        for r in range(rowNumber):
            yield (
                x + initialOffsetX + c * (gapX + sizeX),
                y + initialOffsetY + r * (gapY + sizeY),
            )
