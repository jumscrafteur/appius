import pygame
import random

class Building:
    def __init__(self, pos):
        self.pos = pos
        self.risk_collapse = 0  # 0:pas de risk
        self.number_workers = 0
        self.price_building = 0
        self.service = False
        self.needs = []
        self.tileImage = None
        

    def _get_pos(self):
        return self.pos

    def _get_riskfeu(self):
        return self.riskfeu

    def _get_riskcollapse(self):
        return self.riskcollapse

    def update_riskfeu(self,Prefect):           
        assert(type(Prefect)==Prefect) 
        return 
    
    def update_riskcollapse(self,Engineer):      
        assert(type(Engineer)==Engineer)
        return

class Tent (Building) :
    def __init__(self,pos):
        super.__init__(self,pos)
        self.type='Tent'
        self.capacity=0 #par défaut 
        self.currentNB=0
        self.statut= {"Panneau":1,"Construction":0,"Tent":0,"T_feu":0,"T_collapse":0} # statut du batiment
    
    def up_date_statut(self,): # a faire
        return None
        
    
class prefecture(Building): 
    def __init__(self,pos):
        super.__init__(self,pos)
        self.type='Prefecture'
        self.statut= {"Prefecture":1,"P_feu":0,"P_collapse":0}
    
    def up_date_statut():
        return None        

class water_well(Building): ##puit
    def __inti__(self,pos):
        super.__init__(self,pos)
        self.type='water_well'


class Senat(Building):
    def __init__(self,pos):
        super.__init__(self,pos)
        self.type='Senat'
        self.statut= {"Senat":1,"S_feu":0,"S_collapse":0}
        self.umployment=0
        self.culture_level=0
        self.Peace_level=0
        self.attractivity=0
        self.population=0
    
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
    def __init__(self,pos):
        super.__init__(self,pos)
        self.type='B_Engineering'
        self.statut= {"B":1,"B_feu":0,"B_collapse":0}



''''sousclasse pour les temples'''
class Temples(Building):
    def __init__(self,pos):
        super.__init__(self,pos)
        self.type='Temples'
        self.nb_temples=0

    def rate_satisfaction():        # a faire seulement le nombre des temples et le taille de la mapp

        return 

class Ceres(Temples):
    def __init__(self,pos):
        super.__init__(self,pos)
        self.religion='Ceres'
    
    def rate_satisfaction():        
        return 
        
class Mars(Temples):
    def __init__(self,pos):
        super.__init__(self,pos)
        self.religion='Mars'
    
    def rate_satisfaction():        
        return 
        
class Mercury(Temples):
    def __init__(self,pos):
        super.__init__(self,pos)
        self.religion='Mercury'
    
    def rate_satisfaction():        
        return 
        
class Neptune (Temples):
    def __init__(self,pos):
        super.__init__(self,pos)
        self.religion='Neptune'

    def rate_satisfaction():        
        return 
        
class Venus(Temples):
    def __init__(self,pos):
        super.__init(self,pos)
        self.religon='Venus'
    
    def rate_satisfaction():        
        return 
    
class Buildings:
    def __init__(self):
        ''' Un dict de liste vide '''
        self.listBuilding = {"Tent":[],"Prefecture":[],"B_Engineering":[],"water_well":[],"Senat":[],"Temples":{"Ceres":[],"Mars":[],"Mercury":[],"Neptune":[],"Venus":[]}}

    def __iter__(self):                        #
        return iter(self.Building)

    def add_Tent(self, T): 
        assert(type(T)==Tent)
        self.Building["Tent"].append(T)
    def add_prefecture(self,P):
        assert(type(P)==prefecture)
        self.Building["Prefecture"].append(P)
    def add_B_Engineering(self,B):
        assert(type(B)==B_engineering)
        self.Building["B_Enginneering"].append(B)
    def add_water_well(self,W):
        assert(type(W)==water_well)
        self.Building["water_well"].append(W)
    def add_Senat(self,S):
        assert(type(S)==Senat)
        self.Building["Senat"].append(S)
    def add_Temples(self,Temple):
        if(type(Temple)==Ceres):
            self.Building["Temples"]["Ceres"].append(Temple)
        elif(type(Temple)==Mars):
            self.Building["Temples"]["Mars"].append(Temple)
        elif(type(Temple)==Mercury):
            self.Building["Temples"]["Mercury"].append(Temple)
        elif(type(Temple)==Neptune):
            self.Building["Temples"]["Neptune"].append(Temple)
        elif(type(Temple)==Venus):
            self.Building["Temples"]["Venus"].append(Temple)
        else:
            exit

    def remove_tent(self,T):
        assert(type(T)==Tent)
        self.Building["Tent"].remove(T)
    def remove_prefecture(self,P):
        assert(type(P)==prefecture)
        self.Building["Prefecture"].remove(P)
    def remove_B_Engineering(self,B):
        assert(type(B)==B_engineering)
        self.Building["B_Enginneering"].remove(B)
    def remove_water_well(self,W):
        assert(type(W)==water_well)
        self.Building["water_well"].remove(W)
    def remove_senat(self,S):
        assert(type(S)==Senat)
        self.Building["Senat"].remove(S)
    def remove_temples(self,Temple):
        if(type(Temple)==Ceres):
            self.Building["Temples"]["Ceres"].remove(Temple)
        elif(type(Temple)==Mars):
            self.Building["Temples"]["Mars"].remove(Temple)
        elif(type(Temple)==Mercury):
            self.Building["Temples"]["Mercury"].remove(Temple)
        elif(type(Temple)==Neptune):
            self.Building["Temples"]["Neptune"].remove(Temple)
        elif(type(Temple)==Venus):
            self.Building["Temples"]["Venus"].remove(Temple)
        else:
            exit

class Grass(Building):
    def __init__(self, pos):
        super().__init__(pos)
        self.tileImage = pygame.image.load("newland/Land1a_00285.png")
