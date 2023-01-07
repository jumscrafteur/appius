from Utils import mouse_is_on_map, zone_grid, get_points_in_rectangle
from const import TILE_SIZE, TEMP_TILE
from Building import *
import pygame
import copy


class World:

    def __init__(self, grid_l_x, grid_l_y, width, height, hud, world):
        # props
        self.grid_lx = grid_l_x
        self.grid_ly = grid_l_y
        self.width = width
        self.height = height
        self.hud = hud
        self.world = world
        self.boundary = [self.grid_lx *
                         TILE_SIZE * 2, self.grid_ly * TILE_SIZE]
        # rendering
        self.render = self.creation_surface()
        # etc
        self.temp_tile = []
        self.zone_region = []
        # self.zoom = 1

    def creation_surface(self):
        mapRender = pygame.Surface(
            (self.boundary[0], self.boundary[1]))
        for x in self.world:
            for building in x:
                building.map[0] += self.boundary[0]/2
                mapRender.blit(building.tileImage,
                               (building.map[0], building.map[1]))

        render = {"map": mapRender}
        return render

    def update(self, drag_start, drag_end, mouse_pos, mouse_action, camera):
        drag_process = mouse_action[0]
        if not mouse_action[0] and self.temp_tile != []:
            for temp in self.temp_tile:
                if temp["type"] == "house":
                    self.construction(temp)
                elif temp["type"] == "shovel":
                    self.desstruction(temp)
            self.hud["main"].interaction = None
        self.temp_tile = []
        if self.hud["main"].interaction != None:
            zone = zone_grid(drag_process,
                             drag_start, drag_end, camera.scroll, self.boundary[0]/2)
            if zone != None:
                grid_pos_start, grid_pos_end = zone_grid(
                    drag_process, drag_start, drag_end, camera.scroll, self.boundary[0]/2)
                x1, y1 = grid_pos_start
                x2, y2 = grid_pos_end
                self.zone_region = get_points_in_rectangle(x1, y1, x2, y2)
                for grid_pos in self.zone_region:
                    if mouse_is_on_map(self, grid_pos, mouse_pos):
                        self.temp_tile.append(
                            self.temp_changement(grid_pos, self.hud["main"].interaction))

    def construction(self, temp):
        grid_pos = temp["grid"]
        collision = temp["collision"]
        if not collision:
            self.world.Building[grid_pos[0]].remove(
                self.world.Building[grid_pos[0]][grid_pos[1]])
            self.world.Building[grid_pos[0]].insert(grid_pos[1],
                                                    Housing((grid_pos[0], grid_pos[1])))

            temp = self.world.Building[grid_pos[0]][grid_pos[1]]
            temp.map[0] += self.boundary[0]/2
            self.render["map"].blit(
                temp.tileImage, (temp.map[0], temp.map[1]))

    def desstruction(self, temp):
        grid_pos = temp["grid"]
        collision = temp["collision"]
        temp["type"] = "add"
        if collision:
            self.world.Building[grid_pos[0]].remove(
                self.world.Building[grid_pos[0]][grid_pos[1]])
            self.world.Building[grid_pos[0]].insert(grid_pos[1],
                                                    Grass((grid_pos[0], grid_pos[1])))

            temp = self.world.Building[grid_pos[0]][grid_pos[1]]
            temp.map[0] += self.boundary[0]/2
            self.render["map"].blit(
                temp.tileImage, (temp.map[0], temp.map[1]))

    def temp_changement(self, grid_pos, type_change):
        img = TEMP_TILE[self.hud["main"].interaction]
        img.set_alpha(100)

        render_pos = self.world.Building[grid_pos[0]][grid_pos[1]
                                                      ].map
        iso_poly = self.world.Building[grid_pos[0]][grid_pos[1]
                                                    ].iso_poly
        collision = self.world.Building[grid_pos[0]
                                        ][grid_pos[1]].collision
        # print(
        # f"pos{iso_poly},collision{collision},name{self.world.Building[grid_pos[0]][grid_pos[1]]}")

        temp_tile = {
            "image": img,
            "render_pos": render_pos,
            "iso_poly": iso_poly,
            "collision": collision,
            "type": type_change,
            "grid": (grid_pos[0], grid_pos[1])
        }
        return temp_tile

    def draw_grid(self, camera, screen):
        for x in self.world:
            for building in x:
                grid = building.iso_poly
                grid = [(x + self.boundary[0]/2 + camera.scroll.x, y+camera.scroll.y)
                        for x, y in grid]
                pygame.draw.polygon(screen, (0, 0, 0), grid, 1)

    def draw_temptile(self, temp_tile, camera, screen):
        iso_poly = temp_tile["iso_poly"]
        iso_poly = [(x + self.boundary[0]/2 +
                     camera.scroll.x, y + camera.scroll.y) for x, y in iso_poly]
        if temp_tile["type"] == "house":
            if temp_tile["collision"]:
                pygame.draw.polygon(screen, (255, 0, 0), iso_poly, 6)
            else:
                pygame.draw.polygon(screen, (255, 255, 255), iso_poly, 6)
        elif temp_tile["type"] == "shovel":
            if temp_tile["collision"]:
                pygame.draw.polygon(screen, (255, 255, 0), iso_poly, 6)
        render_pos = temp_tile["render_pos"]
        screen.blit(
            temp_tile["image"],
            (
                render_pos[0] + camera.scroll.x,
                render_pos[1] + camera.scroll.y
            )
        )

    def draw(self, camera, screen):
        screen.fill((0, 0, 0))
        # self.render["map"] = pygame.transform.scale(
        #     self.render["map"],  (self.render["map"].get_width(), self.render["map"].get_width()))
        screen.blit(self.render["map"],
                    (camera.scroll.x, camera.scroll.y))
        for temp_tile in self.temp_tile:
            if temp_tile != None:
                self.draw_temptile(temp_tile, camera, screen)
