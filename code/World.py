from Utils import mouse_is_on_map, zone_grid, get_points_in_rectangle, set_neighborhood_likeliness, road_shifting_util, get_nearby_tile
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
        self.road_system = [[None] * self.grid_lx for _ in range(self.grid_ly)]

    def creation_surface(self):
        mapRender = pygame.Surface(
            (self.boundary[0], self.boundary[1]))
        for x in self.world:
            for building in x:
                if building.name == "road":
                    building.map[0] += self.boundary[0]/2
                    mapRender.blit(building.tileImage[building.current_state],
                                   (building.map[0], building.map[1]))
                else:
                    building.map[0] += self.boundary[0]/2
                    mapRender.blit(building.tileImage,
                                   (building.map[0], building.map[1]))

        render = {"map": mapRender}
        return render

    def update(self, drag_start, drag_end, mouse_pos, mouse_action, camera):
        drag_process = mouse_action[0]
        if not mouse_action[0] and self.temp_tile != []:
            for temp in self.temp_tile:
                if temp is not None:
                    if temp["type"] in ["house"]:
                        self.construction(temp)
                    elif temp["type"] == "shovel":
                        self.destruction(temp)
                    elif temp["type"] == "road":
                        self.cheminement(temp)
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
                        print(grid_pos)
                        self.temp_tile.append(
                            self.temp_changement(grid_pos, self.hud["main"].interaction))

    def cheminement(self, temp):
        grid_pos = temp["grid"]
        collision = temp["collision"]
        if not collision:
            self.world.Building[grid_pos[0]].remove(
                self.world.Building[grid_pos[0]][grid_pos[1]])
            road_entity = Chemins((grid_pos[0], grid_pos[1]))
            # print("---------------")
            # print(
            #     f"before change n{road_entity.north},s{road_entity.south},w{road_entity.west},e{road_entity.east}")
            self.world.Building[grid_pos[0]].insert(grid_pos[1],
                                                    road_entity)
            set_neighborhood_likeliness(
                self.world.Building[grid_pos[0]][grid_pos[1]], self.world.Building)

            road_entity.map[0] += self.boundary[0]/2
            self.render["map"].blit(
                road_entity.tileImage[road_shifting_util(road_entity)], (road_entity.map[0], road_entity.map[1]))
            # print("---------------")
            if road_entity.north:
                x, y = get_nearby_tile(road_entity.grid, "north")
                temporary = self.world.Building[x][y]
                set_neighborhood_likeliness(
                    temporary, self.world.Building)
                self.render["map"].blit(temporary.tileImage[road_shifting_util(
                    temporary)], (temporary.map[0], temporary.map[1]))
            if road_entity.south:
                x, y = get_nearby_tile(road_entity.grid, "south")
                temporary = self.world.Building[x][y]
                set_neighborhood_likeliness(
                    temporary, self.world.Building)
                self.render["map"].blit(temporary.tileImage[road_shifting_util(
                    temporary)], (temporary.map[0], temporary.map[1]))
            if road_entity.west:
                x, y = get_nearby_tile(road_entity.grid, "west")
                temporary = self.world.Building[x][y]
                set_neighborhood_likeliness(
                    temporary, self.world.Building)
                self.render["map"].blit(temporary.tileImage[road_shifting_util(
                    temporary)], (temporary.map[0], temporary.map[1]))
            if road_entity.east:
                x, y = get_nearby_tile(road_entity.grid, "east")
                temporary = self.world.Building[x][y]
                set_neighborhood_likeliness(
                    temporary, self.world.Building)
                self.render["map"].blit(temporary.tileImage[road_shifting_util(
                    temporary)], (temporary.map[0], temporary.map[1]))

    def construction(self, temp):
        grid_pos = temp["grid"]
        collision = temp["collision"]
        if not collision:
            self.world.Building[grid_pos[0]].remove(
                self.world.Building[grid_pos[0]][grid_pos[1]])
            tile_type = type_of_tile(grid_pos, temp["type"])
            self.world.Building[grid_pos[0]].insert(grid_pos[1],
                                                    tile_type)

            temp = self.world.Building[grid_pos[0]][grid_pos[1]]
            temp.map[0] += self.boundary[0]/2
            self.render["map"].blit(
                temp.tileImage, (temp.map[0], temp.map[1]))

    def destruction(self, temp):
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
            north = get_nearby_tile(temp.grid, "north")
            south = get_nearby_tile(temp.grid, "south")
            west = get_nearby_tile(temp.grid, "west")
            east = get_nearby_tile(temp.grid, "east")
            tile_north = self.world.Building[north[0]][north[1]]
            tile_south = self.world.Building[south[0]][south[1]]
            tile_west = self.world.Building[west[0]][west[1]]
            tile_east = self.world.Building[east[0]][east[1]]
            # print(
            #     f"type :: n {type(tile_north)}, s {type(tile_south)}, w {type(tile_west)}, e {type(tile_east)}")
            if type(tile_north) == Chemins:
                set_neighborhood_likeliness(tile_north, self.world.Building)
                self.render["map"].blit(tile_north.tileImage[road_shifting_util(
                    tile_north)], (tile_north.map[0], tile_north.map[1]))
            if type(tile_south) == Chemins:
                set_neighborhood_likeliness(tile_south, self.world.Building)
                self.render["map"].blit(tile_south.tileImage[road_shifting_util(
                    tile_south)], (tile_south.map[0], tile_south.map[1]))
            if type(tile_west) == Chemins:
                set_neighborhood_likeliness(tile_west, self.world.Building)
                self.render["map"].blit(tile_west.tileImage[road_shifting_util(
                    tile_west)], (tile_west.map[0], tile_west.map[1]))
            if type(tile_east) == Chemins:
                set_neighborhood_likeliness(tile_east, self.world.Building)
                self.render["map"].blit(tile_east.tileImage[road_shifting_util(
                    tile_east)], (tile_east.map[0], tile_east.map[1]))

    def temp_changement(self, grid_pos, type_change):
        available = ["house", "shovel", "road"]
        if self.hud["main"].interaction in available:
            img = TEMP_TILE[self.hud["main"].interaction]
            img.set_alpha(100)

            render_pos = self.world.Building[grid_pos[0]][grid_pos[1]
                                                          ].map
            iso_poly = self.world.Building[grid_pos[0]][grid_pos[1]
                                                        ].iso_poly
            collision = self.world.Building[grid_pos[0]
                                            ][grid_pos[1]].collision
            # print(
            #     f"pos{iso_poly},collision{collision},name{self.world.Building[grid_pos[0]][grid_pos[1]]}")

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
        if temp_tile["type"] in ["house", "road"]:
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
        screen.blit(self.render["map"],
                    (camera.scroll.x, camera.scroll.y))
        for temp_tile in self.temp_tile:
            if temp_tile != None:
                self.draw_temptile(temp_tile, camera, screen)
