"""Goal:faire une classe gameUpdate qui pioche les donnés 
de position des tentes et des sprite,respectivement dans 
la clase Buldings et workers
"""   


class Stat:
    def fire_Risks(homeLocation,prefetCurrentLocation):
        Distance_=distance(homeLocation,prefetCurrentLocation)
        if (Distance_>1):
            return 0
       
    def criminality_Risks(homeLocation,prefetOfficeLocation):
        Distance_=distance(homeLocation,prefetOfficeLocation)
        if (Distance_>1:
            return 0
         
    def collapse_Risks(homeLocation,ingineerLocation):
        Distance_=distance(homeLocation,ingineerLocation)
        if (Distance_>1):
            return 0
    def attractivity(fire,collapse,criminality):
        return (300-((fire+collapse+criminality)/300))*100
    
    
    