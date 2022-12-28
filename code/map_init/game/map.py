import pygame as pg
import sys
from .world import World
from .setting import *
from .utils import draw_text
from .camera import Camera
from .gamehud import *
from .Game_event import *


class MapGame:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.width, self.height = self.screen.get_size()
        # world
        self.world = World(40, 40, self.width, self.height)
        # camera
        self.camera = Camera(self.width, self.height, self.world.boundary)
        # hud
        self.grid = True
        self.hudup = Hudupper(0, 0)
        self.hudleft = Hudbigleft(self.width-24, self.height+25)
        self.infofps = InfoShow(
            self.width*0.5, 2, f"fps={round(self.clock.get_fps())}", 18, (255, 255, 255))
        self.infopop = InfoShow(
            self.width*0.6, 2, f"Pop    xxxx", 18, (255, 255, 255))

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(60)
            self.events()
            self.draw()

    def event_key(self):
        self.camera.movement_arrow(pg.key.get_pressed())

    def event_souris(self):
        # mouse_pos = pg.mouse.get_pos()
        # mouse_action = pg.mouse.get_pressed()
        # self.camera.movement_mouse(pg.mouse.get_pos())
        # self.hudleft.action(self.screen)
        pass

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            # if event.type == pg.MOUSEBUTTONDOWN:
            #     self.hudleft.button_123.MouseonButton()
            # if event.type == pg.USEREVENT:
            #     event.action(self.hudleft.button_123.image.copy(
            #     ), pg.mouse.get_pos(), pg.mouse.get_pressed(), self.screen)
        self.event_souris()
        self.event_key()

    def draw(self):
        self.world.draw(self.camera, self.screen)

        self.hudleft.draw(self.screen)
        self.hudup.draw(self.screen)
        self.infofps.draw(self.screen)
        self.infopop.draw(self.screen)

        pg.display.flip()
