
import pygame as pg
import sys


class Camera:

    def __init__(self, width, height):

        self.width = width
        self.height = height

        self.scroll = pg.Vector2(0, 0)
        self.dx = 0
        self.dy = 0
        self.speed = 25
        self.m_up = False
        self.m_down = False
        self.m_left = False
        self.m_right = False

    def movement(self):
        for key in pg.event.get():
            if key.type == pg.KEYDOWN:
                if key.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()
                if key.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                elif key.key == pg.K_UP:
                    self.m_up = True
                elif key.key == pg.K_DOWN:
                    self.m_down = True
                elif key.key == pg.K_RIGHT:
                    self.m_right = True
                elif key.key == pg.K_LEFT:
                    self.m_left = True
            elif key.type == pg.KEYUP:
                if key.key == pg.K_UP:
                    self.m_up = False
                elif key.key == pg.K_DOWN:
                    self.m_down = False
                elif key.key == pg.K_RIGHT:
                    self.m_right = False
                elif key.key == pg.K_LEFT:
                    self.m_left = False
            if self.m_up:
                self.dy = -self.speed
                self.scroll.y += self.dy
            if self.m_down:
                self.dy = self.speed
                self.scroll.y += self.dy
            if self.m_right:
                self.dx = self.speed
                self.scroll.x += self.dx
            if self.m_left:
                self.dx = -self.speed
                self.scroll.x += self.dx
        # update camera scroll
        # self.scroll.x += self.dx
        # self.scroll.y += self.dy
