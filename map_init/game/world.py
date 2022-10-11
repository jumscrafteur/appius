
import pygame as pg
# import random
from .setting import TILE_SIZE


class World:

    def __init__(self, grid_l_x, grid_l_y, width, height):
        self.grid_lx = grid_l_x
        self.grid_ly = grid_l_y
        self.width = width
        self.height = height
        self.tileval = [[13, 22, 20, 27, 00, 00, 00, 31, 00, 00],  # 1
                        [14, 26, 20, 27, 00, 00, 00, 31, 00, 00],  # 2
                        [12, 26, 20, 27, 00, 00, 00, 31, 00, 00],  # 3
                        [11, 26, 30, 23, 00, 00, 00, 31, 00, 00],  # 4
                        [22, 29, 27, 00, 00, 00, 00, 31, 00, 00],  # 5
                        [28, 28, 23, 00, 00, 00, 00, 31, 00, 00],  # 6
                        [00, 00, 00, 00, 00, 00, 00, 31, 00, 35],  # 7
                        [32, 32, 32, 32, 32, 32, 32, 33, 32, 32],  # 8
                        [36, 00, 00, 00, 00, 00, 00, 00, 00, 00],  # 9
                        [00, 00, 00, 00, 00, 00, 00, 00, 00, 00],  # 10
                        ]

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

        #r = random.randint(1, 50)
# # --------
# #   random tile/ map is randomized
# # ----
#         if r <= 9:
#             tile = {"name": "tree1", "offset": 28}
#         elif r > 10 and r <= 15:
#             tile = {"name": "tree2", "offset": 38}
#         elif r > 15 and r <= 18:
#             tile = {"name": "rock1", "offset": 36}
#         elif r > 20 and r <= 25:
#             tile = {"name": "rock2", "offset": 10}
#         else:
#             tile = {"name": "", "offset": 0}

        match self.tileval[grid_x][grid_y]:
            case 11:
                tile = {"name": "tree1", "offset": 14}
            case 12:
                tile = {"name": "tree2", "offset": 19}
            case 13:
                tile = {"name": "rock1", "offset": 18}
            case 14:
                tile = {"name": "rock2", "offset": 5}
            case 20:
                tile = {"name": "water", "offset": 0}
            case 21:
                tile = {"name": "water_e1", "offset": 0}
            case 22:
                tile = {"name": "water_e2", "offset": 0}
            case 23:
                tile = {"name": "water_e3", "offset": 0}
            case 24:
                tile = {"name": "water_e4", "offset": 0}
            case 25:
                tile = {"name": "water_d1", "offset": 3}
            case 26:
                tile = {"name": "water_d2", "offset": 0}
            case 27:
                tile = {"name": "water_d3", "offset": 0}
            case 28:
                tile = {"name": "water_d4", "offset": 0}
            case 29:
                tile = {"name": "water_s1", "offset": 0}
            case 30:
                tile = {"name": "water_s3", "offset": 0}
            case 31:
                tile = {"name": "path1", "offset": 0}
            case 32:
                tile = {"name": "path2", "offset": 0}
            case 33:
                tile = {"name": "path_31", "offset": 0}
            case 35:
                tile = {"name": "flagR", "offset": 23}
            case 36:
                tile = {"name": "flagB", "offset": 23}
            case _:
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
            "appius/map_init/asset_graphis/Land1a_00078.png")
        tree1 = pg.image.load(
            "appius/map_init/asset_graphis/Land1a_00016.png")
        tree2 = pg.image.load(
            "appius/map_init/asset_graphis/Land1a_00045.png")
        rock1 = pg.image.load(
            "appius/map_init/asset_graphis/plateau_00001.png")
        rock2 = pg.image.load(
            "appius/map_init/asset_graphis/plateau_00005.png")
        water = pg.image.load(
            "appius/map_init/asset_graphis/Land1a_00120.png")
        watere1 = pg.image.load(
            "appius/map_init/asset_graphis/Land1a_00145.png")
        watere2 = pg.image.load(
            "appius/map_init/asset_graphis/Land1a_00148.png")
        watere3 = pg.image.load(
            "appius/map_init/asset_graphis/Land1a_00159.png")
        watere4 = pg.image.load(
            "appius/map_init/asset_graphis/Land1a_00153.png")
        waterd1 = pg.image.load(
            "appius/map_init/asset_graphis/Land1a_00135.png")
        waterd2 = pg.image.load(
            "appius/map_init/asset_graphis/Land1a_00136.png")
        waterd3 = pg.image.load(
            "appius/map_init/asset_graphis/Land1a_00128.png")
        waterd4 = pg.image.load(
            "appius/map_init/asset_graphis/Land1a_00141.png")
        waters1 = pg.image.load(
            "appius/map_init/asset_graphis/Land1a_00171.png")
        waters3 = pg.image.load(
            "appius/map_init/asset_graphis/Land1a_00173.png")
        path1 = pg.image.load(
            "appius/map_init/asset_graphis/Land2a_00096.png")
        path2 = pg.image.load(
            "appius/map_init/asset_graphis/Land2a_00093.png")
        path_31 = pg.image.load(
            "appius/map_init/asset_graphis/Land2a_00108.png")
        flagR = pg.image.load(
            "appius/map_init/asset_graphis/Land3a_00085.png")
        flagB = pg.image.load(
            "appius/map_init/asset_graphis/Land3a_00089.png")
        nrock1 = pg.image.load(
            "appius/map_init/asset_graphis/land3a_00074.png")
        nrock2 = pg.image.load(
            "appius/map_init/asset_graphis/land3a_00076.png")
        nrock3 = pg.image.load(
            "appius/map_init/asset_graphis/land3a_00077.png")

        return {"land": land, "tree1": tree1, "tree2": tree2, "rock1": rock1, "rock2": rock2, "water": water,
                "water_e1": watere1, "water_e2": watere2, "water_e3": watere3, "water_e4": watere4,
                "water_d1": waterd1, "water_d2": waterd2, "water_d3": waterd3, "water_d4": waterd4,
                "water_s1": waters1, "water_s3": waters3,
                "path1": path1, "path2": path2, "path_31": path_31,
                "flagR": flagR, "flagB": flagB,
                "nrock1": nrock1, "nrock2": nrock2, "nrock1": nrock2
                }
