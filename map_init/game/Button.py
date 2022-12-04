import pygame
from .Game_event import *
# from const import font1


class Button:

    def __init__(self,  x, y, width, height, action, *args):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.action = action
        self.args = []
        self.box = pg.Rect(self.x, self.y, self.width, self.height)
        self.box.topleft = (self.x, self.y)
        self.clicked = False
        for _i in args:
            self.args.append(_i)

        # self.box.topleft=(x,y)
    # def MouseonButton(self, posMouse):
    #     if (posMouse[0] > (self.x - self.width/2) and posMouse[0] < (self.x + self.width/2)):
    #         if (posMouse[1] > (self.y - self.height/2) and posMouse[1] < (self.y + self.height/2)):
    #             pygame.event.post(pygame.event.Event(
    #                 pygame.USEREVENT, {"action": self.action}))
    #             return 1

    def setAction(self, action, *args):
        self.args = []
        for _i in args:
            self.args.append(_i)
        self.action = action

    def Clicked(self):
        if self.box.collidepoint(pg.mouse.get_pos()):
            if pg.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                self.action(*self.args)
            if pg.mouse.get_pressed()[0] == 0:
                self.clicked = False


class Button_img(Button):
    def __init__(self, x, y, image, action=imprimer):
        self.image = pygame.image.load(image).convert()
        super().__init__(x, y, self.image.get_width(), self.image.get_height(), action)
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.box = self.image.get_rect(center=(self.x, self.y))

    def show(self, screen):
        screen.blit(pygame.transform.scale(
            self.image, (self.image.get_width(), self.image.get_height())), self.rect)


class Button_text(Button):

    def __init__(self, x, y, action, text, font_in="chalkduster.ttf"):
        self.text = text
        font = pygame.font.SysFont(font_in, 60)
        self.font = font
        self.text_render = font.render(
            self.text, 1, (210, 210, 210), (225, 225, 225))
        super().__init__(x, y, self.text_render.get_width(),
                         self.text_render.get_height(), action)

    def show(self, screen, border=None):

        pygame.draw.rect(screen, border, ((self.x-self.text_render.get_width()/2)-2, (self.y -
                         self.text_render.get_height()/2)-2, self.text_render.get_width()+4, self.text_render.get_height()+4), 0)
        screen.blit(self.text_render, (self.x-self.text_render.get_width() /
                    2, self.y-self.text_render.get_height()/2))
