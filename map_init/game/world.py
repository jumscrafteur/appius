
import pygame as pg
# import random
from .setting import *


class World:

    def __init__(self, grid_l_x, grid_l_y, width, height):
        self.grid_lx = grid_l_x
        self.grid_ly = grid_l_y
        self.width = width
        self.height = height
        self.tileval = TILE_VAL

        self.land_tile = pg.Surface(
            (self.grid_lx * TILE_SIZE * 2, self.grid_ly * TILE_SIZE))
        # self.land_tile = pg.Surface((self.width, self.height)).co2nvert_alpha()
        self.tiles = self.load_images()
        self.world = self.cree_world()

        #
        #

    def cree_world(self):
        world = []

        for grid_x in range(self.grid_lx):
            world.append([])
            for grid_y in range(self.grid_ly):
                world_tile = self.grid_to_world(grid_x, grid_y)
                world[grid_x].append(world_tile)

            #
            #           render image alongside with grid init
            #
                render_pos = world_tile["render_pos"]
                self.land_tile.blit(
                    self.tiles["land"], (render_pos[0] + self.land_tile.get_width()*0.5, render_pos[1] + self.land_tile.get_height()*0))
        return world
        #
        #          WORLD=[  [output(0,0),output(0,1)....,output(0,gridy)],
        #                .....
        #                   [output(gridx,0),.....,output(gridx,gridy)]      ]
        #

    def setval(self, r):
        self.tileval = r

    def grid_to_world(self, grid_x, grid_y):

        rect = [
            (grid_x*TILE_SIZE, grid_y*TILE_SIZE),
            (grid_x*TILE_SIZE+TILE_SIZE, grid_y*TILE_SIZE),
            (grid_x*TILE_SIZE+TILE_SIZE, grid_y*TILE_SIZE+TILE_SIZE),
            (grid_x*TILE_SIZE, grid_y*TILE_SIZE+TILE_SIZE)
        ]

        iso_poly = [self.cart_to_iso(x, y) for x, y in rect]

        # find minimum pos for x,y because pygame.surface.blit take arg of
        # the upper left corner of the blit or a Rect when start drawing
        minx = min([x for x, y in iso_poly])
        miny = min([y for x, y in iso_poly])

        output = {
            "grid": [grid_x, grid_y],
            "cart_rect": rect,
            "iso_poly": iso_poly,
            "render_pos": [minx, miny],
            "tile": matchcasetileval(grid_x, grid_y)
        }

        return output

    def cart_to_iso(self, x, y):
        iso_x = x - y
        iso_y = (x + y)/2
        return iso_x, iso_y

    def load_images(self):

        land = LAND1A_078.convert_alpha()
        l1a35 = LAND1A_035.convert_alpha()
        l1a36 = LAND1A_036.convert_alpha()
        l1a49 = LAND1A_049.convert_alpha()
        l1a57 = LAND1A_057.convert_alpha()
        l1a58 = LAND1A_058.convert_alpha()
        l1a60 = LAND1A_060.convert_alpha()
        l1a61 = LAND1A_061.convert_alpha()
        l1a120 = LAND1A_120.convert_alpha()
        l1a128 = LAND1A_128.convert_alpha()
        l1a133 = LAND1A_133.convert_alpha()
        l1a139 = LAND1A_139.convert_alpha()
        l1a143 = LAND1A_143.convert_alpha()
        l1a147 = LAND1A_147.convert_alpha()
        l1a148 = LAND1A_148.convert_alpha()
        l1a152 = LAND1A_152.convert_alpha()
        l1a159 = LAND1A_159.convert_alpha()
        l1a170 = LAND1A_170.convert_alpha()
        l1a171 = LAND1A_171.convert_alpha()
        l1a172 = LAND1A_172.convert_alpha()
        l1a173 = LAND1A_173.convert_alpha()
        l1a234 = LAND1A_234.convert_alpha()
        l1a235 = LAND1A_235.convert_alpha()
        l1a285 = LAND1A_285.convert_alpha()
        l2a095 = LAND2A_095.convert_alpha()
        l3a071 = LAND3A_071.convert_alpha()
        l3a072 = LAND3A_072.convert_alpha()
        l3a074 = LAND3A_074.convert_alpha()
        l3a081 = LAND3A_081.convert_alpha()
        l3a082 = LAND3A_082.convert_alpha()

        return {"land": land,
                "l1a35": l1a35, "l1a36": l1a36, "l1a49": l1a49, "l1a57": l1a57, "l1a58": l1a58, "l1a60": l1a60, "l1a61": l1a61,
                "l1a120": l1a120, "l1a128": l1a128, "l1a133": l1a133, "l1a139": l1a139, "l1a143": l1a143, "l1a147": l1a147, "l1a148": l1a148,
                "l1a152": l1a152, "l1a159": l1a159, "l1a170": l1a170, "l1a171": l1a171, "l1a172": l1a172, "l1a173": l1a173, "l1a234": l1a234,
                "l1a235": l1a235, "12a285": l1a285,
                "l2a095": l2a095,
                "l3a071": l3a071, "l3a072": l3a072, "l3a074": l3a074, "l3a081": l3a081, "l3a082": l3a082}
