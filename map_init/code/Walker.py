from Building import Chemins
import random


class Walker():
    def __init__(self, save):
        self.range = 0
        # self.building = None
        # self.type = None
        # TODO : change to a map class
        self.map = None
        self.path = []
        self.dir = (0, 0)
        self.pos = (0, 0)
        self.rayonDAction = 0
        self.unemployed = True  # unemployed pour définir la statut d'un walker

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

        isNextPosInRange = len(grid[0]) > nextPos[0] >= 0 and\
            len(grid) > nextPos[1] >= 0

        isNextPosAPath = False
        if isNextPosInRange:
            isNextPosAPath = type(grid[nextPos[1]][nextPos[0]]) == Chemins

        isNextPosBackward = dir == (self.dir[0]*-1, self.dir[1]*-1)

        return isNextPosInRange and isNextPosAPath and not isNextPosBackward

    def work():
        # NE PAS MODIFIER
        return


class Engineer(Walker):
    def __init__(self, save):
        Walker.__init__(self, save)
        self.type = "Engineer"
        self.unemployed = False

    def work(self, Buildings):
        assert(type(Buildings) == Buildings)
        r = self.rayonDAction
        for i in range(self.pos[0]-r, self.pos[0]+r):
            for j in range(self.pos[1]-r, self.pos[1]+r):
                for b in Buildings.listBuilding.keys():                 # a refaire
                    for k in Buildings.listBuilding[b]:
                        if ((i, j) == k.pos) and (k.risk_collapse > 0):
                            k._set_risk_collapse(0)


class Prefect(Walker):
    def __init__(self, save):
        Walker.__init__(self, save)
        self.type = "Prefect"
        self.unemployed = False

    def work(self, Buildings):
        r = self.rayonDAction
        assert(type(Buildings) == Buildings)
        for i in range(self.pos[0]-r, self.pos[0]+r):  # a refaire
            for j in range(self.pos[1]-r, self.pos[1]+r):
                for b in Buildings.listBuilding:
                    if ((i, j) == b.pos) and (b.risk_fire > 0):
                        b._set_riskfire(0)


class Citizen(Walker):
    def __init__(self, save):
        Walker.__init__(self, save)
        self.type = "Citizen"

    def work(self, Buildings):
        assert(type(Buildings) == Buildings)
        r = self.rayonDAction
        for i in range(self.pos[0]-r, self.pos[0]+r):
            for j in range(self.pos[1]-r, self.pos[1]+r):
                for b in Buildings.listBuilding:
                    if(b.type == 'Tent'):
                        if ((i, j) == b.pos) and (b.currentNB < b.capacity):
                            b.updateNB()
                            break


class Walkers():
    # une sorte de base de donnée pour les Walkers
    # sauvegarde des Walkers dans un dict selon leurs types
    # sauvegarde des citizen dans une liste
    def __init__(self):
        self.listWalker = {"Citizen": [], "Prefect": [], "Engineer": []}
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
            if(i.unemployed):
                nb += 1
        return nb/self._get_pop(self)

    # Gestion des citizens
    def ajout_Citizen(self, C):
        assert(type(C) == Citizen)
        self.ListWalker["Citizen"].append(C)

    def supp_Citizen(self, C):
        assert(type(C) == Citizen)
        self.ListWalker["Citizen"].remove(C)

    # Gestion de Prefet
    def ajout_Prefet(self, P):
        assert(type(P) == Prefect)
        self.ListWalker["Prefect"].append(P)

    def supp_Prefet(self, P):
        assert(type(P) == Prefect)
        self.ListWalker["Prefect"].remove(P)

    # Gestion de Engineer
    def ajout_Engineer(self, E):
        assert(type(E) == Engineer)
        self.ListWalker["Engineer"].append(E)

    def supp_Engineer(self, E):
        assert(type(E) == Engineer)
        self.ListWalker["Engineer"].remove(E)
