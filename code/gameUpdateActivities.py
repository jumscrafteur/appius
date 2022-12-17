"""
@author: yacin
"""
# Ce code permet de retourner la l'attractivité et la 
#prospérité en %

import Buildings

class gameUpdate:
    building=list(Buildings.building)
    def attractivity(fireRisk,collapseRisks,criminalityRisks):
        return (1.5-((fireRisk+collapseRisks+criminalityRisks)/1.5))*100
    
    def prosperity(building):
        sumActractivities=0
        for i in building:
            sumActractivities+=gameUpdate.attractivity(i.risk_fire,i.risk_collapse,i.risk_criminality)
        return sumActractivities/len(building)
