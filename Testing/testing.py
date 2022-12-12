import pygame as pg
import sys
SCREEN = WIDTH, HEIGH = 300, 300

pg.init()
run = True
display = pg.display.set_mode(SCREEN)


def eventhandling():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()


while run:
    eventhandling()
