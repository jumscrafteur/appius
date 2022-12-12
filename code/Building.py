class Building:
    def __init__(self):
        self.pos = (0, 0)
        self.type = None  # {Tent,Temples,Prefecture,Well-water..}
        self.risk_collapse = 0  # 0:pas de risk 
        self.capacity = 0
        self.number_workers = 0
        self.price_building = 0
        self.currentNB = 0
        self.service =False
        self.needs =[]

    def position(self):
        return

class Buildings:
    def __init__(self):
        ''' Une simple liste vide '''
        self.Building = []

    def ajouter(self, Building):  #ajouter 
        self.Building.append(Building)

    def retirer(self, Building):
        self.Building.remove(Building)