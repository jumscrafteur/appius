
import pygame as pg
import random
from .setting import TILE_SIZE


class World:

    def __init__(self, grid_l_x, grid_l_y, width, height):
        self.grid_lx = grid_l_x
        self.grid_ly = grid_l_y
        self.width = width
        self.height = height

        self.land_tile = pg.Surface((self.width, self.height))

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
                    self.tiles["land"], (render_pos[0] + self.width/2, render_pos[1] + self.height/4))

        return world
        #
        #          WORLD=[  [output(0,0),output(0,1)....,output(0,gridy)],
        #                .....
        #                   [output(gridx,0),.....,output(gridx,gridy)]      ]
        #

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

        r = random.randint(1, 50)
# --------
#   random tile/ map is randomized
# ----
        if r <= 9:
            tile = {"name": "tree1", "offset": 28}
        elif r > 10 and r <= 15:
            tile = {"name": "tree2", "offset": 38}
        elif r > 15 and r <= 18:
            tile = {"name": "rock1", "offset": 36}
        elif r > 20 and r <= 25:
            tile = {"name": "rock2", "offset": 10}
        else:
            tile = {"name": "", "offset": 0}

        output = {
            "grid": [grid_x, grid_y],
            "cart_rect": rect,
            "iso_poly": iso_poly,
            "render_pos": [minx, miny],
            "tile": tile
        }

        return output

    def cart_to_iso(self, x, y):
        iso_x = x - y
        iso_y = (x + y)/2
        return iso_x, iso_y

    #           OUT-DATED: small tiles
    # def load_images(self):

    #     land = pg.image.load("appius/map_init/asset_graphis_graphis/Land1a_00078.png")
    #     tree1 = pg.image.load("appius/map_init/asset_graphis_graphis/Land1a_00016.png")
    #     tree2 = pg.image.load("appius/map_init/asset_graphis_graphis/Land1a_00045.png")
    #     rock1 = pg.image.load("appius/map_init/asset_graphis_graphis/plateau_00001.png")
    #     rock2 = pg.image.load("appius/map_init/asset_graphis_graphis/plateau_00005.png")
    #     #land2 = pg.image.load("appius/map_init/asset_graphis_graphis/Land1a_00003.png")

    #     return {"land": land, "tree1": tree1, "tree2": tree2, "rock1": rock1, "rock2": rock2}

    #       2x upscale of shits

    def load_images(self):

        land = pg.image.load(
            "appius/map_init/asset_graphis/Land1a_00078_2X.png")
        tree1 = pg.image.load(
            "appius/map_init/asset_graphis/Land1a_00016_2X.png")
        tree2 = pg.image.load(
            "appius/map_init/asset_graphis/Land1a_00045_2X.png")
        rock1 = pg.image.load(
            "appius/map_init/asset_graphis/plateau_00001_2X.png")
        rock2 = pg.image.load(
            "appius/map_init/asset_graphis/plateau_00005_2X.png")
        #land2 = pg.image.load("appius/map_init/asset_graphis_graphis/Land1a_00003.png")

        return {"land": land, "tree1": tree1, "tree2": tree2, "rock1": rock1, "rock2": rock2}
