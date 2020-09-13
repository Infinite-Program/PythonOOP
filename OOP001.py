#Created by Infinite-Program
#Creating a class using OOP

#Class names usually have capital letters
class Crop:
    """A generic food crop"""
    
    #Constructor(Function)
    def __init__(self,growthRate,lightNeed,waterNeed):
        
        #Attributes(Variables)Prefix = self.
        
        self._daysGrowing = 0
        self._growthRate = growthRate
        self._lightNeed = lightNeed
        self._waterNeed = waterNeed
        self._status = "Seed"
        self._type = "Generic"
        
        #Above attributes have been prefixed with underscores
        #to indicate that they are private.
        
def main():
    #Instantiate the class
    newCrop = Crop(1,4,3)
    
main()
        
        
        