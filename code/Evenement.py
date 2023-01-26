import pygame
from const import FIRE_THRESHOLD, COLLAPSE_THESHOLD, BURNING_TIME
from Building import Housing, Tent
from Walker import Walker


class Evenement:

    def __init__(self) -> None:
        self.timer = pygame.time.get_ticks()
        self.game_speed = 1
        self.day = 0.025

        self.day_pass = 0
        self.month = self.day_pass / 5
        self.year = self.month / 12
        self.path_index = 0

    def calendar_update(self):
        self.day_pass += self.day*self.game_speed

    def change_game_speed(self, speed):
        self.game_speed = speed

    def change_building_timer(self, listonFire):
        for building in listonFire:
            if building.onFire:
                building.time_under_effect += self.day*self.game_speed

    def change_risk_fire(self, listBuilding):
        for building in listBuilding:
            if building.canFire:
                # print(f"risk{building.risk_fire}")
                building.risk_fire += self.day*self.game_speed

    def set_on_fire(self, listBuilding):
        for building in listBuilding:
            # print(f"risk{building.onFire,building.canRemove}")
            if building.risk_fire >= FIRE_THRESHOLD and building.canFire:
                # print("setOnfire")
                building.onFire = True
                building.useless = True
                building.canRemove = False
                building.canFire = False

    def done_burning(self, listonFire):
        # print(listonFire)
        for building in listonFire:
            # print(f"risk{building.onFire},timer{building.time_under_effect}")

            if building.time_under_effect >= BURNING_TIME:
                # print("done buring")
                building.canRemove = True
                building.onFire = False

    def vacane_slot(self, world, listWalker, road_system, offset):

        for building in world.listBuilding:
            if type(building) == Housing:
                if building.available:
                    spawning = Walker((20, 39))
                    spawning.goal = building.grid
                    spawning.path_finding(road_system)
                    spawning.my_house = building
                    listWalker.append(spawning)
                    building.available = False

        for walker in listWalker:
            print(walker.my_house, world.listBuilding)
            if walker.my_house not in world.listBuilding:
                walker.goal = (20, 0)
                if walker.my_house != None:
                    walker.path_finding(road_system)
                    walker.path_index = 0
                    walker.my_house = None
            arrived = self.walker_move(walker)
            if arrived:
                if walker.my_house != None:
                    self.building_sign_to_house(
                        walker.pos, world.Building, world.listBuilding, offset)
                listWalker.remove(walker)

    def building_sign_to_house(self, pos, Building, listBuilding, offset):
        x, y = pos
        if Building[x][y] in listBuilding:
            listBuilding.remove(Building[x][y])
        Building[x].remove(Building[x][y])
        Building[x].insert(y, Tent((x, y)))
        Building[x][y].map[0] += offset
        listBuilding.append(Building[x][y])

    def walker_move(self, walker):
        # print(walker.path_index)
        # sprint(walker.path)
        if walker.path_index >= len(walker.path):
            return True
        new_pos = walker.path[int(walker.path_index)]
        walker.pos = new_pos
        walker.path_index += self.day*self.game_speed

        return False

    def update(self, world, listWalker, road_system, offset):
        self.calendar_update()
        self.change_risk_fire(world.listBuilding)
        self.set_on_fire(world.listBuilding)
        self.change_building_timer(world.listonFire)
        self.done_burning(world.listonFire)
        self.vacane_slot(world, listWalker, road_system, offset)
