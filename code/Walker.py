class Walker():
    def __init__(self, save):
        self.range = 0
        self.building = None
        self.type = None
        # TODO : change to a map class
        self.map = None
        self.path = []
        self.dir = (0, 0)
        self.pos = (0, 0)

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
    
    
    def work(self,save):
        MR=save.map.layers["risk_feu"] #donne la matirce a modifier
        r=self.rayonDAction
        for i in range(self.pos[0]-r,self.pos[0]+r):
            for j in range(self.pos[1]-r,self.pos[1]+r):
                MR[i][j]==0	 
        
		

class Prefect(Walker):
    def __init__(self,save):
	    Walker.__init__(self, save)
        self.type = "Prefect"
        

    def work():
        #work of prefect
        return 
    
class Citizen(Walker):
    def __init__(self,save):
	    Walker.__init__(self, save)
        self.type = "Citizen"
         
         
         
    def work():
        #work of Citizen
        return 