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
        self.unemployed = True # unemployed pour définir la statut d'un walker 

    def move():
        # TODO :https://www.notion.so/Syst-me-de-mouvement-d89eda3bfd07423aac03172de8d46827
        return

    def work():
        # NE PAS MODIFIER
        return


class Engineer(Walker):
    def __init__(self, save):
        Walker.__init__(self, save)
        self.type = "Engineer"

    def work(self, Buildings):
        assert(type(Buildings)==Buildings) #ca pour forcer que le builfdings est de type Buildings qui est la listee des batiments 
        r = self.rayonDAction
        for i in range(self.pos[0]-r, self.pos[0]+r):
            for j in range(self.pos[1]-r, self.pos[1]+r):
                for b in Buildings.building:
                    if ((i, j) == b.pos) and (b.risk_collapse > 0):
                        b.risk_collapse = 0
      


class Prefect(Walker):
    def __init__(self,save):
        Walker.__init__(self,save)
        self.type = "Prefect"

    def work(self,save):
        MR = save.layers["risk_feu"] 
        r = self.rayonDAction
        for i in range(self.pos[0]-r, self.pos[0]+r):
            for j in range(self.pos[1]-r, self.pos[1]+r):
                MR[i][j] = 0


class Citizen(Walker):
    def __init__(self,save):
        Walker.__init__(self, save)
        self.type = "Citizen"

    def work(self, save, Buildings):
        r = self.rayonDAction
        assert(type(Buildings)==Buildings) # de meme ici 
        for i in range(self.pos[0]-r, self.pos[0]+r):
            for j in range(self.pos[1]-r, self.pos[1]+r):
                for b in Buildings.building:
                    if ((i, j) == b.pos) and (b.currentNB < b.capacity):
                        b.currentNb += 1
                        break   