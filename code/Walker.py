from Building import Chemins
import random
import pygame
from const import *
from Utils import cartCoToIsoCo, A_star


class Walker():
    def __init__(self, spawnpoint=(0, 0), goal=None):

        self.range = 0
        # self.building = None
        # self.type = None
        self.map = None
        self.path = []
        self.dir = (0, 0)
        self.pos = spawnpoint
        self.rayonDAction = 0
        self.unemployed = True  # unemployed pour définir la statut d'un walker
        self.sprite = pygame.image.load(
            "Walkers/Citizen01/Citizen01_00001.png").convert_alpha()
        self.path = [self.pos]
        self.goal = goal
        self.path_index = 0
        self.my_house = None

    def mouv(self, grid):
        self.dir = self.getRandomValideDir(grid)

        self.pos = (self.pos[0] + self.dir[0],
                    self.pos[1] + self.dir[1])

    def getRandomValideDir(self, grid):
        dirs = [dir for dir in [(0, -1), (1, 0), (0, 1), (-1, 0)]
                if self.isNextPosValide(dir, grid)]
        return random.choice(dirs if (len(dirs) > 0) else [(self.dir[0]*-1, self.dir[1]*-1)])

    def isNextPosValide(self, dir, grid):
        nextPos = (self.pos[0] + dir[0],
                   self.pos[1] + dir[1])

        isNextPosInRange = MAP_SIZE[0] > nextPos[0] >= 0 and\
            MAP_SIZE[1] > nextPos[1] >= 0

        isNextPosAPath = False
        if isNextPosInRange:

            isNextPosAPath = grid[nextPos[0]][nextPos[1]] == True
            # isNextPosAPath = type(grid[nextPos[0]][nextPos[1]]) == Chemins

        isNextPosBackward = dir == (self.dir[0]*-1, self.dir[1]*-1)

        return isNextPosInRange and isNextPosAPath and not isNextPosBackward

    def work():
        # NE PAS MODIFIER
        return

    def draw(self, camera, screen, world):
        cell_relative = world.Building[self.pos[0]][self.pos[1]]
        pos_x = cell_relative.map[0]
        pox_y = cell_relative.map[1]
        screen.blit(self.sprite.convert_alpha(),
                    (pos_x+camera.scroll.x, pox_y+camera.scroll.y))

    def path_finding(self, grid):
        if self.goal != None:
            self.path = A_star(
                (self.pos[0], self.pos[1]), (self.goal[0], self.goal[1]), grid)
            self.dirs = [(0, -1)]+[(self.path[i+1][0] - self.path[i][0], self.path[i+1][1] - self.path[i][1])
                                   for i in range(len(self.path) - 1)]


class Engineer(Walker):
    def __init__(self, save):
        Walker.__init__(self, save)
        self.type = "Engineer"
        self.unemployed = False

    def work(self, Buildings):
        assert (type(Buildings) == Buildings)
        r = self.rayonDAction
        for i in range(self.pos[0]-r, self.pos[0]+r):
            for j in range(self.pos[1]-r, self.pos[1]+r):
                for b in Buildings.listBuilding.keys():                 # a refaire
                    for k in Buildings.listBuilding[b]:
                        if ((i, j) == k.grid) and (k.risk_collapse > 0):
                            k._set_risk_collapse(0)


class Prefect(Walker):
    def __init__(self, spawnpoint=(0, 0), goal=None):
        super().__init__(spawnpoint, goal)
        self.type = "Prefect"
        self.unemployed = False
        self.headquarter = None
        self.missionaire = None
        self.returning = False
        self.rayonDAction = 2
        self.sprite = pygame.image.load(
            "Walkers/Prefec/citizen02_00615.png").convert_alpha()

    def work(self, listBuilding):
        r = self.rayonDAction

        # assert (type(Buildings) == Buildings)
        for i in range(self.pos[0]-r, self.pos[0]+r):  # a refaire
            for j in range(self.pos[1]-r, self.pos[1]+r):
                for b in listBuilding:
                    if ((i, j) == b.grid) and (b.risk_fire > 0):
                        b._set_riskfire(0)


class Citizen(Walker):
    def __init__(self, spawnpoint=(0, 0), goal=None):
        super().__init__(spawnpoint, goal)
        self.type = "Citizen"

    def work(self, Buildings):
        assert (type(Buildings) == Buildings)
        r = self.rayonDAction
        for i in range(self.pos[0]-r, self.pos[0]+r):
            for j in range(self.pos[1]-r, self.pos[1]+r):
                for b in Buildings.listBuilding:
                    if (b.type == 'Tent'):
                        if ((i, j) == b.grid) and (b.currentNB < b.capacity):
                            b.updateNB()
                            break


class Walkers():
    # une sorte de base de donnée pour les Walkers
    # sauvegarde des Walkers dans un dict selon leurs types
    # sauvegarde des citizen dans une liste
    def __init__(self):
        self.listWalker = {"Citizen": [], "Prefect": [],
                           "Engineer": [], "Immigrant": []}
        self.pop = 0

    def _get_pop(self):
        return self.pop

    def _set_pop(self, p):
        self.pop = p

    def calcul_pop(self):
        self.pop = len(self.listWalker["Citizen"])+len(
            self.listWalker["Prefect"])+len(self.listWalker["Engineer"])

    def unemployment_rate(self):
        l = self.listWalker["Citizen"]
        self.calcul_pop
        assert self.pop > 0, "la population est nulle"
        nb = 0
        for i in l:
            if (i.unemployed):
                nb += 1
        return nb/self._get_pop(self)

    # Gestion des citizens
    def ajout_Citizen(self, C):
        assert (type(C) == Citizen)
        self.listWalker["Citizen"].append(C)

    def supp_Citizen(self, C):
        assert (type(C) == Citizen)
        self.listWalker["Citizen"].remove(C)

    # Gestion de Prefet
    def ajout_Prefet(self, P):
        assert (type(P) == Prefect)
        self.listWalker["Prefect"].append(P)

    def supp_Prefet(self, P):
        assert (type(P) == Prefect)
        self.listWalker["Prefect"].remove(P)

    # Gestion de Engineer
    def ajout_Engineer(self, E):
        assert (type(E) == Engineer)
        self.listWalker["Engineer"].append(E)

    def supp_Engineer(self, E):
        assert (type(E) == Engineer)
        self.listWalker["Engineer"].remove(E)
