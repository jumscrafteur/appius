
from const import *
from Utils import cartCoToIsoCo
TILE_SIZE = 60


def type_of_tile(grid, name):
    x, y = grid
    match name:
        case "house":
            return Housing((x, y))


class Building:
    def __init__(self, pos):
        self.grid = pos
        self.grid_x, self.grid_y = pos
        self.rect = [
            (self.grid_x*TILE_SIZE, self.grid_y*TILE_SIZE),
            (self.grid_x*TILE_SIZE+TILE_SIZE, self.grid_y*TILE_SIZE),
            (self.grid_x*TILE_SIZE+TILE_SIZE, self.grid_y*TILE_SIZE+TILE_SIZE),
            (self.grid_x*TILE_SIZE, self.grid_y*TILE_SIZE+TILE_SIZE)
        ]
        self.iso_poly = [cartCoToIsoCo(x, y) for x, y in self.rect]
        min_x = min([x for x, y in self.iso_poly])
        min_y = min([y for x, y in self.iso_poly])
        self.map = [min_x, min_y]
        self.type = None  # {Tent,Temples,Prefecture,Well-water..}
        self.risk_collapse = 0  # 0:pas de risk
        self.capacity = 0
        self.number_workers = 0
        self.price_building = 0
        self.currentNB = 0
        self.service = False
        self.needs = []
        self.collision = True

        self.tileImage = None
        self.type = None

    # def position(self):
    #     return

    def _get_riskfeu(self):
        return self.riskfeu

    def _get_riskcollapse(self):
        return self.riskcollapse

    def _set_riskfire(self, n):
        self.risk_fire = n

    def _set_risk_criminality(self, n):
        self.risk_criminality = n

    def _set_risk_collapse(self, n):
        self.risk_collapse = n


class Tent (Building):
    def __init__(self, pos):
        super.__init__(self, pos)
        self.type = 'Tent'
        self.capacity = 5  # par défaut
        self.currentNB = 0
        self.statut = {"Panneau": 1, "Construction": 0, "Tent": 0,
                       "T_feu": 0, "T_collapse": 0}  # statut du batiment

    def update_NB(self):
        self.currentNB += 1

    def up_date_statut(self):  # a faire
        self.statut
        return None


class prefecture(Building):
    def __init__(self, pos):
        super.__init__(self, pos)
        self.type = 'Prefecture'
        self.statut = {"Prefecture": 1, "P_feu": 0, "P_collapse": 0}

    def up_date_statut():
        return None


class water_well(Building):  # puit
    def __inti__(self, pos):
        super.__init__(self, pos)
        self.type = 'water_well'


class Senat(Building):
    def __init__(self, pos):
        super.__init__(self, pos)
        self.type = 'Senat'
        self.statut = {"Senat": 1, "S_feu": 0, "S_collapse": 0}
        self.umployment = 0
        self.culture_level = 0
        self.Peace_level = 0
        self.attractivity = 0
        self.population = 0

    def calcul_culture_level(self):
        return

    def calcul_Peace_level(self):
        return

    def calcul_attractuvity(self):
        return

    def calcul_populaton(self):
        return

    def up_date_statut():
        return None


class B_engineering(Building):
    def __init__(self, pos):
        super.__init__(self, pos)
        self.type = 'B_Engineering'
        self.statut = {"B": 1, "B_feu": 0, "B_collapse": 0}


''''sousclasse pour les temples'''


class Temples(Building):
    def __init__(self, pos):
        super.__init__(self, pos)
        self.type = 'Temples'
        self.nb_temples = 0

    def rate_satisfaction():        # a faire seulement le nombre des temples et le taille de la mapp

        return


class Ceres(Temples):
    def __init__(self, pos):
        super.__init__(self, pos)
        self.religion = 'Ceres'

    def rate_satisfaction():
        return


class Mars(Temples):
    def __init__(self, pos):
        super.__init__(self, pos)
        self.religion = 'Mars'

    def rate_satisfaction():
        return


class Mercury(Temples):
    def __init__(self, pos):
        super.__init__(self, pos)
        self.religion = 'Mercury'

    def rate_satisfaction():
        return


class Neptune (Temples):
    def __init__(self, pos):
        super.__init__(self, pos)
        self.religion = 'Neptune'

    def rate_satisfaction():
        return


class Venus(Temples):
    def __init__(self, pos):
        super.__init(self, pos)
        self.religon = 'Venus'

    def rate_satisfaction():
        return


class Buildings:
    def __init__(self):
        ''' Une simple liste vide '''
        self.listBuilding = []

    def ajouter(self, B):
        self.Building.append(B)

    def retirer(self, B):
        self.Building.remove(B)

    def __iter__(self):                        #
        return iter(self.Building)


class Grass(Building):
    def __init__(self, pos):
        super().__init__(pos)
        self.name = "grass"
        self.imageoffset = 0
        self.collision = False

        self.tileImage = pygame.image.load(
            "newland/Land1a_00285.png").convert_alpha()


class Chemins(Building):
    def __init__(self, pos):
        super().__init__(pos)
        self.name = "road"
        self.imageoffset = 0
        self.collision = True
        self.north = False
        self.south = False
        self.west = False
        self.east = False

        self.tileImage = {"N": pygame.image.load("Chemins/N.png").convert_alpha(), "S": pygame.image.load("Chemins/S.png").convert_alpha(), "E": pygame.image.load("Chemins/E.png").convert_alpha(), "W": pygame.image.load("Chemins/W.png").convert_alpha(),
                          "N&E": pygame.image.load("Chemins/N&E.png").convert_alpha(), "S&E": pygame.image.load("Chemins/S&E.png").convert_alpha(), "W&N": pygame.image.load("Chemins/W&N.png").convert_alpha(), "W&S": pygame.image.load("Chemins/W&S.png").convert_alpha(),
                          "N_S_E": pygame.image.load("Chemins/N_S_E.png").convert_alpha(), "N_W_S": pygame.image.load("Chemins/N_W_S.png").convert_alpha(), "W_N_E": pygame.image.load("Chemins/W_N_E.png").convert_alpha(), "W_S_E": pygame.image.load("Chemins/W_S_E.png").convert_alpha(),
                          "S-N": pygame.image.load("Chemins/S-N.png").convert_alpha(), "W-E": pygame.image.load("Chemins/W-E.png").convert_alpha(),
                          "ALL": pygame.image.load("Chemins/ALL.png").convert_alpha()
                          }


class Housing(Building):
    def __init__(self, pos):
        super().__init__(pos)
        self.name = "house"
        self.imageoffset = 0
        self.collision = True

        self.tileImage = pygame.image.load(
            "fonction_render/house/Housng1a_00045.png").convert_alpha()


class Buildings:
    def __init__(self):
        ''' Une simple liste vide '''
        self.Building = []
        self.list = []

    def __iter__(self):
        return iter(self.Building)

    def ajouter(self, Building):  # ajouter
        self.list.append(Building)

    def retirer(self, Buiding):
        self.list.remove(Buiding)
