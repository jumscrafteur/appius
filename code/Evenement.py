import pygame
from const import FIRE_THRESHOLD, COLLAPSE_THESHOLD, BURNING_TIME


class Evenement:

    def __init__(self) -> None:
        self.game_speed = 1

    def change_game_speed(self, speed):
        self.game_speed = speed

    def change_building_timer(self, listonFire):
        for building in listonFire:
            if building.onFire:
                building.time_under_effect += 0.05*self.game_speed

    def change_risk_fire(self, listBuilding):
        for building in listBuilding:
            if building.canFire:
                # print(f"risk{building.risk_fire}")
                building.risk_fire += 0.025*self.game_speed

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

    def update(self, world):
        self.change_risk_fire(world.listBuilding)
        self.set_on_fire(world.listBuilding)
        self.change_building_timer(world.listonFire)
        self.done_burning(world.listonFire)
