
import pygame as pg
import sys


class Camera:

    def __init__(self, width, height):

        self.width = width
        self.height = height

        self.scroll = pg.Vector2(0, 0)
        self.dx = 0
        self.dy = 0
        self.speed = 10
        self.m_up = False
        self.m_down = False
        self.m_left = False
        self.m_right = False

    def movement(self):
        for key in pg.event.get():
            if key.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if key.type == pg.KEYDOWN:
                if key.key == pg.K_ESCAPE:
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
            if key.type == pg.KEYUP:
                if key.key == pg.K_UP:
                    self.m_up = False
                elif key.key == pg.K_DOWN:
                    self.m_down = False
                elif key.key == pg.K_RIGHT:
                    self.m_right = False
                elif key.key == pg.K_LEFT:
                    self.m_left = False
            if self.m_up:
                self.dy = self.speed
            elif self.m_down:
                self.dy = -self.speed
            else:
                self.dy = 0
            if self.m_right:
                self.dx = -self.speed
                # self.scroll.x = self.dx
            elif self.m_left:
                self.dx = self.speed
            else:
                self.dx = 0
                # self.scroll.x = self.dx

        # mouse_pos = pg.mouse.get_pos()

        # # x movement
        # if mouse_pos[0] > self.width * 0.97:
        #     self.dx = -self.speed
        # elif mouse_pos[0] < self.width * 0.03:
        #     self.dx = self.speed
        # else:
        #     self.dx = 0

        # # y movement
        # if mouse_pos[1] > self.height * 0.97:
        #     self.dy = -self.speed
        # elif mouse_pos[1] < self.height * 0.03:
        #     self.dy = self.speed
        # else:
        #     self.dy = 0

        # update camera scroll
        self.scroll.x += self.dx
        self.scroll.y += self.dy
