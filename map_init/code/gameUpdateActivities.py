"""
@author: yacin
"""
# Ce code permet de retourner la l'attractivité et la 
#prospérité en %

import Buildings
    

class gameUpdate:
    def attractivity(fireRisk,collapseRisks,criminalityRisks):
        return (1.5-((fireRisk+collapseRisks+criminalityRisks)/1.5))*100
    
    def prosperity(buildings):
        sumActractivities=0
        for i in buildings:
            sumActractivities+=gameUpdate.attractivity(i.risk_fire,i.risk_collapse,i.risk_criminality)
        return sumActractivities/len(buildings)
while game_Running:
    time.sleep(30)
    for i in list(Buildings.building):
        i.fireRisk=
        i.collapseRisks=
        i.criminalityRisks=
        Attractivity=gameUpdate.attractivity(i.fireRisk, i.collapseRisks, i.criminalityRisks)     
    Prosperity=gameUpdate.prosperity(Buildings.building)