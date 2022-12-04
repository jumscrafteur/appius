import pygame as pg
from .Button import *
from .Game_event import *


class InfoShow:
    def __init__(self, x, y, text, font_size, color):
        self.x = x
        self.y = y
        self.text = text
        self.font_size = font_size
        self.color = color
        self.box = pg.image.load(
            "appius/ingamehud/paneling_00015.png").convert_alpha()

    def draw(self, screen):
        screen.blit(self.box, (self.x, self.y))
        font = pg.font.SysFont(None, self.font_size)
        text_surface = font.render(self.text, True, self.color)
        text_rect = pygame.Rect(
            self.x+10, self.y+5, text_surface.get_width(), text_surface.get_height())
        screen.blit(text_surface, text_rect)


class Hudupper:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pg.image.load(
            "appius/ingamehud/paneling_00235.png").convert_alpha()

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        screen.blit(self.image, (self.x+117, self.y))
        screen.blit(self.image, (self.x+234, self.y))
        screen.blit(self.image, (self.x+351, self.y))
        screen.blit(self.image, (self.x+438, self.y))
        screen.blit(self.image, (self.x+490, self.y))
        screen.blit(self.image, (self.x+585, self.y))
        screen.blit(self.image, (self.x+702, self.y))
        screen.blit(self.image, (self.x+819, self.y))
        screen.blit(self.image, (self.x+936, self.y))
        screen.blit(self.image, (self.x+1053, self.y))
        screen.blit(self.image, (self.x+1170, self.y))


class Hudstick:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pg.image.load(
            "appius/ingamehud/paneling_00014.png").convert_alpha()

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        screen.blit(self.image, (self.x, self.y+24))
        screen.blit(self.image, (self.x, self.y+48))
        screen.blit(self.image, (self.x, self.y+72))
        screen.blit(self.image, (self.x, self.y+95))
        screen.blit(self.image, (self.x, self.y+119))
        screen.blit(self.image, (self.x, self.y+142))
        screen.blit(self.image, (self.x, self.y+166))
        screen.blit(self.image, (self.x, self.y+190))
        screen.blit(self.image, (self.x, self.y+214))
        screen.blit(self.image, (self.x, self.y+238))
        screen.blit(self.image, (self.x, self.y+262))
        screen.blit(self.image, (self.x, self.y+286))
        screen.blit(self.image, (self.x, self.y+310))
        screen.blit(self.image, (self.x, self.y+334))
        screen.blit(self.image, (self.x, self.y+358))
        screen.blit(self.image, (self.x, self.y+382))
        screen.blit(self.image, (self.x, self.y+406))
        screen.blit(self.image, (self.x, self.y+430))
        screen.blit(self.image, (self.x, self.y+454))
        screen.blit(self.image, (self.x, self.y+478))
        screen.blit(self.image, (self.x, self.y+502))
        screen.blit(self.image, (self.x, self.y+526))
        screen.blit(self.image, (self.x, self.y+550))
        screen.blit(self.image, (self.x, self.y+574))
        screen.blit(self.image, (self.x, self.y+598))
        screen.blit(self.image, (self.x, self.y+622))
        screen.blit(self.image, (self.x, self.y+646))
        screen.blit(self.image, (self.x, self.y+670))
        screen.blit(self.image, (self.x, self.y+694))
        screen.blit(self.image, (self.x, self.y+718))
        screen.blit(self.image, (self.x, self.y+742))
        screen.blit(self.image, (self.x, self.y+766))
        screen.blit(self.image, (self.x, self.y+790))
        screen.blit(self.image, (self.x, self.y+814))


class Hudbigleft:
    def __init__(self, width, height):

        self.width = width
        self.height = height
        self.paneling_017 = pg.image.load(
            "appius/ingamehud/paneling_00017.png").convert_alpha()
        self.map_panels_00003 = pg.image.load(
            "appius/ingamehud/map_panels_00003.png").convert_alpha()
        self.panelwindow_013 = pg.image.load(
            "appius/ingamehud/panelwindows_00013.png").convert_alpha()
        #hud in out
        self.button_098 = Button_img(
            self.width-20, 20+21, "appius/ingamehud/paneling_00098.png")
        # gap 77/ 2 long af button
        self.button_080 = Button_img(
            self.width-120, 170+21, "appius/ingamehud/paneling_00080.png")
        self.button_082 = Button_img(
            self.width-43, 170+21,  "appius/ingamehud/paneling_00082.png")
        # gap 39 /small button
        self.button_085 = Button_img(
            self.width-139, 199+21,  "appius/ingamehud/paneling_00085.png")
        self.button_088 = Button_img(
            self.width-100, 199+21,  "appius/ingamehud/paneling_00088.png")
        self.button_091 = Button_img(
            self.width-62, 199+21,  "appius/ingamehud/paneling_00091.png")
        self.button_094 = Button_img(
            self.width-23, 199+21,  "appius/ingamehud/paneling_00094.png")
        # gap width 50 gap height 36 /big button
        self.button_123 = Button_img(
            self.width-130, 294+21,  "appius/ingamehud/paneling_00123.png")
        self.button_131 = Button_img(
            self.width-80, 294+21, "appius/ingamehud/paneling_00131.png")
        self.button_135 = Button_img(
            self.width-30, 294+21,  "appius/ingamehud/paneling_00135.png")
        #
        self.button_127 = Button_img(
            self.width-130, 330+21,  "appius/ingamehud/paneling_00127.png")
        self.button_163 = Button_img(
            self.width-80, 330+21,  "appius/ingamehud/paneling_00163.png")
        self.button_151 = Button_img(
            self.width-30, 330+21,  "appius/ingamehud/paneling_00151.png")
        #

        self.button_147 = Button_img(
            self.width-130, 366+21,  "appius/ingamehud/paneling_00147.png")
        self.button_143 = Button_img(
            self.width-80, 366+21,  "appius/ingamehud/paneling_00143.png")
        self.button_139 = Button_img(
            self.width-30, 366+21,  "appius/ingamehud/paneling_00139.png")
        #
        self.button_167 = Button_img(
            self.width-130, 402+21,  "appius/ingamehud/paneling_00167.png")
        self.button_159 = Button_img(
            self.width-80, 402+21,  "appius/ingamehud/paneling_00159.png")
        self.button_155 = Button_img(
            self.width-30, 402+21,  "appius/ingamehud/paneling_00155.png")
        #
        self.button_246 = Button_img(
            self.width-130, 438+21,  "appius/ingamehud/paneling_00246.png")
        self.button_115 = Button_img(
            self.width-80, 436+21,  "appius/ingamehud/paneling_00115.png")
        self.button_122 = Button_img(
            self.width-30, 436+21,  "appius/ingamehud/paneling_00122.png")
        #
        self.mini_button = {"098": self.button_098, "080": self.button_080, "082": self.button_082, "085":
                            self.button_085, "088": self.button_088, "091": self.button_091, "094": self.button_094, }
        #

    def draw(self, screen):
        screen.blit(self.paneling_017, (self.width - 162, 4+21))
        screen.blit(self.map_panels_00003, (self.width - 162, 450+4+21))
        screen.blit(self.map_panels_00003, (self.width - 162, 1000))
        screen.blit(self.panelwindow_013, (self.width-162+6, 216+4+21))
        # hud move in move out
        self.button_098.show(screen)
        # 2 long button
        self.button_080.show(screen)
        self.button_082.show(screen)
        # 4 mini button
        self.button_085.show(screen)
        self.button_088.show(screen)
        self.button_091.show(screen)
        self.button_094.show(screen)
        # 15 big button
        # l1
        self.button_123.show(screen)
        self.button_131.show(screen)
        self.button_135.show(screen)
        # l2
        self.button_127.show(screen)
        self.button_163.show(screen)
        self.button_151.show(screen)
        # l3
        self.button_147.show(screen)
        self.button_143.show(screen)
        self.button_139.show(screen)
        # l4
        self.button_167.show(screen)
        self.button_159.show(screen)
        self.button_155.show(screen)
        # l5
        self.button_246.show(screen)
        self.button_115.show(screen)
        self.button_122.show(screen)

    def action(self, grid):
        self.button_098.setAction(toggle_grid_2_5D, grid)
        self.button_098.Clicked()
