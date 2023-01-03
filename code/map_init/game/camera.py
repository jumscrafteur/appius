
import pygame as pg
import sys


class Camera:

    def __init__(self, width, height, boundary):
        assert False, "deprecated code , do not use it"

        self.width = width
        self.height = height

        self.scroll = pg.Vector2(0, 0)
        self.dx = 0
        self.dy = 0
        self.mx = 0
        self.my = 0
        self.m_speed = 10
        self.k_speed = 5
        self.m_up = False
        self.m_down = False
        self.m_left = False
        self.m_right = False

    def movement_arrow(self, key_press):
        # map boundary
        if self.scroll.x > self.width*0.05:
            self.scroll.x = self.width*0.05
        elif self.scroll.x < -self.width*1.2:
            self.scroll.x = -self.width*1.2
        elif self.scroll.y > self.height*0.08:
            self.scroll.y = self.height*0.08
        elif self.scroll.y < -self.height*0.65:
            self.scroll.y = -self.height*0.65
        self.scroll.x += (key_press[pg.K_LEFT] -
                          key_press[pg.K_RIGHT])*self.k_speed
        self.scroll.y += (key_press[pg.K_UP]-key_press[pg.K_DOWN])*self.k_speed

    def movement_mouse(self, mouse_pos):

        # x movement
        if mouse_pos[0] > self.width * 0.97:
            self.mx = -self.m_speed
        elif mouse_pos[0] < self.width * 0.03:
            self.mx = self.m_speed
        else:
            self.mx = 0

        # y movement
        if mouse_pos[1] > self.height * 0.97:
            self.my = -self.m_speed
        elif mouse_pos[1] < self.height * 0.03:
            self.my = self.m_speed
        else:
            self.my = 0
        # map boundary
        if self.scroll.x > self.width*0.05:
            self.scroll.x = self.width*0.05
        elif self.scroll.x < -self.width*1.2:
            self.scroll.x = -self.width*1.2
        elif self.scroll.y > self.height*0.08:
            self.scroll.y = self.height*0.08
        elif self.scroll.y < -self.height*0.65:
            self.scroll.y = -self.height*0.65
        # update camera scroll
        self.scroll.x += self.mx
        self.scroll.y += self.my
