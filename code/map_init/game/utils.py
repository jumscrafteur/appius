import pygame as pg


def draw_text(screen, text, size, color, pos):
    font = pg.font.SysFont(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(topleft=pos)

    screen.blit(text_surface, text_rect)


def cartCoToIsoCo(cartX, cartY):
    isoX = cartX - cartY
    isoY = (cartX + cartY)/2
    return isoX, isoY


def isoCoToCartCo(isoX, isoY):
    cartX = isoY + isoX/2
    cartY = isoY - isoX/2
    return cartX, cartY
