class Stat():
    def fire_Risks(homeLocation,prefetCurrentLocation):
        Distance_=Distance(homeLocation,prefetCurrentLocation)
        if (Distance_>10):
            return 0.5
        elif (Distance_>10):
            return 0.4
        elif (Distance_>10):
            return 0.2
        elif (Distance_>10):
            return 0
        return False
    def criminality_Risks(homeLocation,prefetOfficeLocation):
        Distance_=Distance(homeLocation,prefetOfficeLocation)
        if (Distance_>10):
            return 0.5
        elif (Distance_>10):
            return 0.4
        elif (Distance_>10):
            return 0.2
        elif (Distance_>10):
            return 0
        return False 
    def collapse_Risks(homeLocation,ingineerOfficeLocation):
        Distance_=Distance(homeLocation,ingineerOfficeLocation)
        if (Distance_>10):
            return 0.5
        elif (Distance_>10):
            return 0.4
        elif (Distance_>10):
            return 0.2
        elif (Distance_>10):
            return 0
        return Falses
    def attractivity(fire,collapse,criminality):
        return (1.5-((fire+collapse,criminality)/1.5))*100,"%"
    
    def Distance(x1,y1,x2,y2):
        return abs(x2-x1)+abs(y2-y1)
        
        
    