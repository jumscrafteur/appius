from Utils import mouse_is_on_map, mouse_to_grid, get_road_pathway, \
    zone_grid, get_points_in_rectangle, set_neighborhood_likeliness, road_shifting_util, get_nearby_tile,\
    A_star, overlay_util
from const import TILE_SIZE, TEMP_TILE, GRASS_IMAGE, JUST_A_BURNING_MEMORY, RUMBLE_OF_BUILDING, OVERLAY
from Building import *
import pygame


class World:

    def __init__(self, grid_l_x, grid_l_y, width, height, hud, world, save):
        # props
        self.grid_lx = grid_l_x
        self.grid_ly = grid_l_y
        self.width = width
        self.height = height
        self.hud = hud
        self.world = world
        self.save = save
        self.boundary = [self.grid_lx *
                         TILE_SIZE * 2, self.grid_ly * TILE_SIZE]
        # fonctionality
        self.buildable = ["house", "hammer", "water", "sword"]
        self.available = ["shovel", "house",
                          "hammer", "water", "sword", "road"]
        # rendering
        self.render = self.creation_surface()
        # etc
        self.temp_tile = []
        # self.road_build_pathway = []
        self.zone_region = []
        self.on_mouse_temp = None
        # self.zoom = 1
        self.road_system = [[None] * self.grid_lx for _ in range(self.grid_ly)]
        # mini_map
        self.grid = False
        self.overlay_mode = "normal"

    def creation_surface(self):
        mapRender = pygame.Surface(
            (self.boundary[0], self.boundary[1]))
        gridRender = pygame.Surface(
            (self.boundary[0], self.boundary[1]), pygame.SRCALPHA)
        for x in self.world.Building:
            for building in x:
                grid = building.iso_poly
                grid = [(x + self.boundary[0]/2, y)
                        for x, y in grid]
                pygame.draw.polygon(gridRender, (0, 0, 0), grid, 1)
                if building.name == "road":
                    building.map[0] += self.boundary[0]/2
                    mapRender.blit(building.tileImage[road_shifting_util(building)],
                                   (building.map[0], building.map[1]))

                else:
                    building.map[0] += self.boundary[0]/2
                    mapRender.blit(GRASS_IMAGE.convert_alpha(),
                                   (building.map[0], building.map[1]-building.imageOffset))

        render = {"map": mapRender, "grid": gridRender}
        return render

    def update(self, drag_start, drag_end, mouse_pos, mouse_action, camera, mini_map):
        drag_process = mouse_action[0]
        self.on_mouse_temp = None
        if not mouse_action[0] and self.temp_tile != []:

            for temp in self.temp_tile:
                if temp is not None:
                    if temp["type"] in self.buildable:
                        self.construction(temp, mini_map)
                    elif temp["type"] == "shovel":
                        self.destruction(temp, mini_map)
                    elif temp["type"] == "road":
                        self.cheminement(temp, mini_map)
            self.hud["main"].interaction = None
        self.temp_tile = []
        if self.hud["main"].interaction != None:
            on_mouse_grid = mouse_to_grid(
                mouse_pos[0], mouse_pos[1], camera.scroll, self.boundary[0]/2)
            if mouse_is_on_map(self, on_mouse_grid, mouse_pos):
                self.on_mouse_temp = self.temp_changement(
                    on_mouse_grid, self.hud["main"].interaction, "on_mouse")

            zone = zone_grid(drag_process,
                             drag_start, drag_end, camera.scroll, self.boundary[0]/2)
            if zone != None:
                grid_pos_start, grid_pos_end = zone
                x1, y1 = grid_pos_start
                x2, y2 = grid_pos_end

                # special building pattern for road

                if self.hud["main"].interaction == "road":
                    self.zone_region = A_star((x1, y1), (x2, y2))

                    for grid_pos in self.zone_region:
                        if mouse_is_on_map(self, grid_pos, mouse_pos):

                            self.temp_tile.append(
                                self.temp_changement(grid_pos, self.hud["main"].interaction, "drag_drop_road"))

                # others build
                else:
                    if self.hud["main"].interaction in ["house", "shovel"]:
                        self.zone_region = get_points_in_rectangle(
                            x1, y1, x2, y2)
                    else:
                        self.zone_region = [(x2, y2)]
                    for grid_pos in self.zone_region:
                        if mouse_is_on_map(self, grid_pos, mouse_pos):

                            self.temp_tile.append(
                                self.temp_changement(grid_pos, self.hud["main"].interaction, "drag_drop_house"))

    def cheminement(self, temp, mini_map):
        grid_pos = temp["grid"]
        collision = temp["collision"]
        if not collision:
            if self.save.PO >= 4:
                self.world.Building[grid_pos[0]].remove(
                    self.world.Building[grid_pos[0]][grid_pos[1]])
                road_entity = Chemins((grid_pos[0], grid_pos[1]))
                # print("---------------")
                # print(
                #     f"before change n{road_entity.north},s{road_entity.south},w{road_entity.west},e{road_entity.east}")
                road_entity.map[0] += self.boundary[0]/2
                self.world.Building[grid_pos[0]].insert(grid_pos[1],
                                                        road_entity)
                self.road_system[grid_pos[0]][grid_pos[1]] = True
                set_neighborhood_likeliness(
                    self.world.Building[grid_pos[0]][grid_pos[1]], self.world.Building)
                # road_entity.map[0] += self.boundary[0]/2
                self.render["map"].blit(
                    road_entity.tileImage[road_shifting_util(road_entity)], (road_entity.map[0], road_entity.map[1]))

                # print("---------------")
                if road_entity.north:
                    x, y = get_nearby_tile(road_entity.grid, "north")
                    if 0 <= x <= 39 and 0 <= y <= 39:
                        temporary = self.world.Building[x][y]
                        set_neighborhood_likeliness(
                            temporary, self.world.Building)
                        self.render["map"].blit(temporary.tileImage[road_shifting_util(
                            temporary)], (temporary.map[0], temporary.map[1]))
                if road_entity.south:
                    x, y = get_nearby_tile(road_entity.grid, "south")
                    if 0 <= x <= 39 and 0 <= y <= 39:
                        temporary = self.world.Building[x][y]
                        set_neighborhood_likeliness(
                            temporary, self.world.Building)
                        self.render["map"].blit(temporary.tileImage[road_shifting_util(
                            temporary)], (temporary.map[0], temporary.map[1]))
                if road_entity.west:
                    x, y = get_nearby_tile(road_entity.grid, "west")
                    if 0 <= x <= 39 and 0 <= y <= 39:
                        temporary = self.world.Building[x][y]
                        set_neighborhood_likeliness(
                            temporary, self.world.Building)
                        self.render["map"].blit(temporary.tileImage[road_shifting_util(
                            temporary)], (temporary.map[0], temporary.map[1]))
                if road_entity.east:
                    x, y = get_nearby_tile(road_entity.grid, "east")
                    if 0 <= x <= 39 and 0 <= y <= 39:
                        temporary = self.world.Building[x][y]
                        set_neighborhood_likeliness(
                            temporary, self.world.Building)
                        self.render["map"].blit(temporary.tileImage[road_shifting_util(
                            temporary)], (temporary.map[0], temporary.map[1]))

                # mini_map
                grid = road_entity.iso_poly
                mini_map.update_surface(grid, "road")

                # réduction de l'argent
                self.save.PO -= 4

    def construction(self, temp, mini_map):
        grid_pos = temp["grid"]
        collision = temp["collision"]
        if not collision:
            tile_type = type_of_tile(grid_pos, temp["type"])
            if self.save.PO >= tile_type.price_building:
                if tile_type.size == 1:
                    tile_type._construct_me(
                        self.world, self.boundary[0]/2)
                    self.world.listBuilding.append(tile_type)
                elif tile_type.size == 2:
                    tile_type._contruct_big_house(
                        self.world, self.boundary[0]/2)
                temp = self.world.Building[grid_pos[0]][grid_pos[1]]

                grid = temp.iso_poly
                mini_map.update_surface(grid, "building")
                # réduction de l'argent
                self.save.PO -= tile_type.price_building

    def destruction(self, temp, mini_map):
        grid_pos = temp["grid"]
        collision = temp["collision"]
        if collision:
            if self.save.PO >= 2:
                type_check = self.world.Building[grid_pos[0]][grid_pos[1]]
                if type_check.canRemove:
                    if type_check.size == 1:
                        type_check._destroy_me(
                            self.world, self.boundary[0]/2)
                    elif type_check.size == 2:
                        type_check._destroy_big_house(
                            self.world, self.boundary[0]/2)
                    # temp = self.world.Building[grid_pos[0]][grid_pos[1]]

                    # self.render["map"].blit(
                    #     temp.tileImage, (temp.map[0], temp.map[1]))
                    if type(type_check) == Chemins:
                        temp = self.world.Building[grid_pos[0]][grid_pos[1]]

                        self.render["map"].blit(
                            temp.tileImage, (temp.map[0], temp.map[1]))
                        self.road_system[grid_pos[0]][grid_pos[1]] = None
                        north = get_nearby_tile(temp.grid, "north")
                        south = get_nearby_tile(temp.grid, "south")
                        west = get_nearby_tile(temp.grid, "west")
                        east = get_nearby_tile(temp.grid, "east")
                        if 0 <= north[0] <= 39 and 0 <= north[1] <= 39:
                            tile_north = self.world.Building[north[0]][north[1]]
                            if type(tile_north) == Chemins:
                                set_neighborhood_likeliness(
                                    tile_north, self.world.Building)
                                self.render["map"].blit(tile_north.tileImage[road_shifting_util(
                                    tile_north)], (tile_north.map[0], tile_north.map[1]))
                        if 0 <= south[0] <= 39 and 0 <= south[1] <= 39:
                            tile_south = self.world.Building[south[0]][south[1]]
                            if type(tile_south) == Chemins:
                                set_neighborhood_likeliness(
                                    tile_south, self.world.Building)
                                self.render["map"].blit(tile_south.tileImage[road_shifting_util(
                                    tile_south)], (tile_south.map[0], tile_south.map[1]))
                        if 0 <= west[0] <= 39 and 0 <= west[1] <= 39:
                            tile_west = self.world.Building[west[0]][west[1]]
                            if type(tile_west) == Chemins:
                                set_neighborhood_likeliness(
                                    tile_west, self.world.Building)
                                self.render["map"].blit(tile_west.tileImage[road_shifting_util(
                                    tile_west)], (tile_west.map[0], tile_west.map[1]))
                        if 0 <= east[0] <= 39 and 0 <= east[1] <= 39:
                            tile_east = self.world.Building[east[0]][east[1]]
                            if type(tile_east) == Chemins:
                                set_neighborhood_likeliness(
                                    tile_east, self.world.Building)
                                self.render["map"].blit(tile_east.tileImage[road_shifting_util(
                                    tile_east)], (tile_east.map[0], tile_east.map[1]))
                    # else:

                    #     if type_check in self.world.listBuilding:
                    #         self.world.listBuilding.remove(type_check)
                    # mini_map
                    grid = type_check.iso_poly
                    mini_map.update_surface(grid, "grass")
                    # réduction de l'argent
                    self.save.PO -= 2

    def temp_changement(self, grid_pos, type_change, mode):
        if type_change in self.available:
            if mode == "drag_drop_house" and type_change in self.buildable:
                img = TEMP_TILE["blank"]
                img.set_alpha(100)
            else:
                img = TEMP_TILE[type_change]
                img.set_alpha(150)

            render_pos = self.world.Building[grid_pos[0]][grid_pos[1]
                                                          ].map
            iso_poly = self.world.Building[grid_pos[0]][grid_pos[1]
                                                        ].iso_poly
            collision = self.world.Building[grid_pos[0]
                                            ][grid_pos[1]].collision
            offset = img.get_height() - TILE_SIZE
            print(
                f"pos{iso_poly},collision{collision},name{self.world.Building[grid_pos[0]][grid_pos[1]]}")

            temp_tile = {
                "image": img,
                "render_pos": render_pos,
                "iso_poly": iso_poly,
                "collision": collision,
                "type": type_change,
                "grid": (grid_pos[0], grid_pos[1]),
                "offset": offset,

            }
            return temp_tile

    def update_live_event(self):
        self.set_building_on_fire()
        self.turn_building_to_rumble()

    def set_building_on_fire(self):
        for building in self.world.listBuilding:
            if building.onFire:
                self.world.listBuilding.remove(building)
                self.world.listonFire.append(building)

    def an_burning_sensation_animation(self, building, time, camera, screen):
        animation = time % 8
        screen.blit(RUMBLE_OF_BUILDING, (
                    building.map[0]+camera.scroll.x, building.map[1]+camera.scroll.y))
        screen.blit(JUST_A_BURNING_MEMORY[animation], (
                    building.map[0]+camera.scroll.x+JUST_A_BURNING_MEMORY[animation].get_width()/4, building.map[1]-JUST_A_BURNING_MEMORY[animation].get_width()/8+camera.scroll.y))

    def turn_building_to_rumble(self):
        for building in self.world.listonFire:
            if building.useless and not building.onFire:
                self.world.listonFire.remove(building)
                grid_pos = building.grid
                self.world.Building[grid_pos[0]].remove(
                    self.world.Building[grid_pos[0]][grid_pos[1]])
                rumble = type_of_tile(grid_pos, "rumble")
                rumble.map[0] = building.map[0]
                self.world.Building[grid_pos[0]].insert(grid_pos[1],
                                                        rumble)

                self.world.listBuilding.append(rumble)

    def draw_grid(self, camera, screen):
        screen.blit(self.render["grid"],
                    (camera.scroll.x, camera.scroll.y))

    # seulement pour visualization, pas affecte le logique du building
    def draw_temptile(self, temp_tile, camera, screen):
        iso_poly = temp_tile["iso_poly"]
        iso_poly = [(x + self.boundary[0]/2 +
                     camera.scroll.x, y + camera.scroll.y) for x, y in iso_poly]
        if temp_tile["type"] in self.buildable or temp_tile["type"] == "road":
            if temp_tile["collision"]:
                pygame.draw.polygon(screen, (255, 0, 0), iso_poly, 6)
            else:
                pygame.draw.polygon(screen, (255, 255, 255), iso_poly, 6)
        elif temp_tile["type"] == "shovel":
            if temp_tile["collision"]:
                pygame.draw.polygon(screen, (150, 0, 0, 100), iso_poly)
        render_pos = temp_tile["render_pos"]
        offset = temp_tile["offset"]
        screen.blit(
            temp_tile["image"],
            (
                render_pos[0] + camera.scroll.x,
                render_pos[1] + camera.scroll.y - offset
            )
        )
    #
    # seulement pour visualization, pas affecte le logique du building

    def draw_on_mouse_temptile(self, temp_tile, camera, screen):
        iso_poly = temp_tile["iso_poly"]
        iso_poly = [(x + self.boundary[0]/2 +
                     camera.scroll.x, y + camera.scroll.y) for x, y in iso_poly]
        if temp_tile["type"] in self.buildable or temp_tile["type"] == "road":
            if temp_tile["collision"]:
                pygame.draw.polygon(screen, (200, 0, 0), iso_poly)
            else:
                pygame.draw.polygon(screen, (0, 200, 51), iso_poly)
        elif temp_tile["type"] == "shovel":
            if temp_tile["collision"]:
                pygame.draw.polygon(screen, (150, 0, 0), iso_poly)
        render_pos = temp_tile["render_pos"]
        offset = temp_tile["offset"]
        screen.blit(
            temp_tile["image"],
            (
                render_pos[0] + camera.scroll.x,
                render_pos[1] + camera.scroll.y - offset
            )
        )

    def draw_building(self, camera, screen):
        # temp = self.world.listBuilding
        # self.world.listBuilding = sorted(
        #     sorted(
        #         temp, key=lambda temp: temp.grid_x), key=lambda temp: temp.grid_y)
        for building in self.world.listBuilding:
            if building.tileImage != None:
                if building.size == 1:
                    screen.blit(building.tileImage, (
                        building.map[0]+camera.scroll.x, building.map[1]+camera.scroll.y-building.imageOffset))
                else:
                    screen.blit(building.tileImage, (
                        building.map[0]+camera.scroll.x-building.imageOffset_x, building.map[1]+camera.scroll.y-building.imageOffset_y))

    def draw_burning_and_collapse(self, camera, screen, time):
        for building in self.world.listonFire:
            self.an_burning_sensation_animation(building, time, camera, screen)

    def draw_overlay_pillar(self, screen, camera):
        for building in self.world.listBuilding:
            if not building.useless and building.tileImage != None:
                screen.blit(OVERLAY["fond"], (
                    building.map[0]+camera.scroll.x, building.map[1]+camera.scroll.y))
                if building.canFire:
                    percentage = overlay_util(building.risk_fire)
                    if percentage != None:
                        screen.blit(OVERLAY[percentage], (building.map[0]+camera.scroll.x-OVERLAY[percentage].get_width()/2+building.tileImage.get_width()/2,
                                    building.map[1]+camera.scroll.y-OVERLAY[percentage].get_height()+OVERLAY["fond"].get_height()*0.8))
            elif building.tileImage == None:
                screen.blit(OVERLAY["big_fond"], (
                    building.map[0]+camera.scroll.x, building.map[1]+camera.scroll.y))
            else:
                screen.blit(RUMBLE_OF_BUILDING, (
                    building.map[0]+camera.scroll.x, building.map[1]+camera.scroll.y))

    def layer_1_draw(self, camera, screen):
        screen.fill((0, 0, 0))
        screen.blit(self.render["map"],
                    (camera.scroll.x, camera.scroll.y))

    def layer_3_draw(self, camera, screen, time):
        temp = self.world.listBuilding
        self.world.listBuilding = sorted(
            sorted(
                temp, key=lambda temp: temp.grid_x), key=lambda temp: temp.grid_y)
        # print(f"listbuilding:{self.world.listBuilding}")
        # print(f"onFire :{self.world.listonFire}")
        if self.grid:
            self.draw_grid(camera, screen)
        self.draw_burning_and_collapse(camera, screen, time)
        if self.overlay_mode == "normal":
            self.draw_building(camera, screen)
        elif self.overlay_mode == "fire":
            self.draw_overlay_pillar(screen, camera)

    def layer_4_draw(self, camera, screen):
        for temp_tile in self.temp_tile:
            if temp_tile != None:
                self.draw_temptile(temp_tile, camera, screen)
        if self.on_mouse_temp != None:
            self.draw_on_mouse_temptile(self.on_mouse_temp, camera, screen)
