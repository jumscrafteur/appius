class Building:
    def __init__(self):
     self.pos= (0, 0)
     self.type=None # {Tent,Temples,Prefecture,Well-water..}
     self.risk_collapse=0 # 0:pas de risk
     self.capacity=0
     self.currentNB=0
    def position(self)
      return   
  
class Buildings:
        def __init__(self):
        ''' Une simple liste vide '''
          self.Building = []
        def ajouter(self,Building):
          self.Building.append(Building)
        def retirer(self,Building):
           self.Building.remove(Building)
           
           

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
        self.rayonDAction=0

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
        
    def work(self,Buildings):
        while (self.move()):
            for i in range(self.pos[0]-r,self.pos[0]+r):
             for j in range(self.pos[1]-r,self.pos[1]+r):
                 for b in Buildings.building :
                 if ((i,j) == b.pos) and (b.risk_collapse>0):
                     b.risk_collapse == 0
        break
	 
        
		

class Prefect(Walker):
    def __init__(self):
	    Walker.__init__(self)
        self.type ="Prefect"
        
    def work(self):
        MR=save.layers["risk_feu"] #donne la matirce a modifier
        r=self.rayonDAction
        for i in range(self.pos[0]-r,self.pos[0]+r):
            for j in range(self.pos[1]-r,self.pos[1]+r):
                MR[i][j]==0
    
class Citizen(Walker):
    def __init__(self,save,Tents):
	    Walker.__init__(self, save)
        self.type = "Citizen"
        
  def work(self,save,Buildings):
        while (self.move()):
            for i in range(self.pos[0]-r,self.pos[0]+r):
             for j in range(self.pos[1]-r,self.pos[1]+r):
                 for b in Buildings.building :
                 if ((i,j) == b.pos) and (b.currentNB<b.capacity) :
                       b.currentNb+=1
                       break