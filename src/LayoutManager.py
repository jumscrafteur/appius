import pygame


def drawCenter(destSurface: pygame.surface.Surface, srcSurface: pygame.surface.Surface):
    destSurfaceSize = destSurface.get_size()
    srcSurfaceSize = srcSurface.get_size()

    centerPosition = (
        destSurfaceSize[0] / 2 - srcSurfaceSize[0] / 2,
        destSurfaceSize[1] / 2 - srcSurfaceSize[1] / 2,
    )

    destSurface.blit(srcSurface, centerPosition)
