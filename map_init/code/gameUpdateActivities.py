"""
@author: yacin
"""
# Dans while game_Running:
    
# Ce code permet de retourner la l'attractivité et la 
#prospérité en %

import BuildingBrouillon
import Walker


class gameUpdate:
    if CompteurFps%60==0:
        #update les atributs des batiments
        for i in Buildings.building:
            i.fireRisk=fire_Risks(i.pos,Prefect().pos)
            i.collapseRisks=collapse_Risks(i.pos,getMinDistance(Engineer().pos)
            i.criminalityRisks=criminality_Risks(i.pos,getMinDistanceBetwiHomes(i.pos,"Prefecture"))
            Attractivity=gameUpdate.attractivity(i.fireRisk, i.collapseRisks, i.criminalityRisks)     
        Prosperity=gameUpdate.prosperity(Buildings.building)
        
    def attractivity(fireRisk,collapseRisks,criminalityRisks):
        return (1.5-((fireRisk+collapseRisks+criminalityRisks)/1.5))*100
    
    def prosperity(buildings): 
        sumActractivities=0
        for i in buildings:
            sumActractivities+=gameUpdate.attractivity(i.risk_fire,i.risk_collapse,i.risk_criminality)
        return sumActractivities/len(buildings)

    def getMinDistanceWolkerAndHome(homePosition,typeWalker):#renvoie la position du walker le plus proche d'une tente
        listWolkers=Walkers.ListWalker[typeWalker]
        indexMin=0
        for i in range(len(listWolkers)-1): 
            if Distance(homePosition,listWolkers[i+1].pos)<Distance(homePosition,listWolkers[i].pos):
                indexMin=i+1
        return listWolkers[idexMin].pos
            
    def getMinDistanceBetwiHomes(homePosition,TypeLocation):#renvoi le batiment le plus proche d'une position lié à une tente
        listTypeLocation=[]
        for i in Buildings.building:
           if i.type==TypeLocation:
               listTypeLocation.append(i)
        indexMin=0
        for i in range(len(listTypeLocation)-1): 
            if Distance(homePosition,listTypeLocation[i+1].pos)<Distance(homePosition,listTypeLocation[i].pos):
                indexMin=i+1
        return listTypeLocation[idexMin].pos
    
    
S
            