import pygame


class Building:
    def __init__(self, pos):
        self.pos = pos
        self.type = None  # {Tent,Temples,Prefecture,Well-water..}
        self.risk_collapse = 0  # 0:pas de risk
        self.capacity = 0
        self.number_workers = 0
        self.price_building = 0
        self.currentNB = 0
        self.service = False
        self.needs = []

        self.tileImage = None

    # def position(self):
    #     return


class Grass(Building):
    def __init__(self, pos):
        super().__init__(pos)
        # self.tileImage = pygame.image.load("newland/Land1a_00285.png")
        self.tileImage = pygame.image.load("newland/Land1a_00035.png")


class Buildings:
    def __init__(self):
        ''' Une simple liste vide '''
        self.Building = []

    def __iter__(self):
        return iter(self.Building)

    def ajouter(self, Building):  # ajouter
        self.Building.append(Building)

    def retirer(self, Building):
        self.Building.remove(Building)
