from util import Util
class Id:

    def __init__(self, name=None):
        self.name = name
        self.type = self.setType()        

    def __str__(self):
        aux = "<ID> \n"

        if self.name:
            aux += self.name + "\n"
        
        aux += "</ID> \n"
        return aux
    
    def __repr__(self):
        return self.__str__()

    def setType(self):
        return {
            'i': int,
            's': str,
            'b': bool,
            'f': float,
            'd': float,
            'o': object
        }[self.name[0]]
        
    def getName(self):
        return self.name

    def getType(self):
        return self.type

    def getValue(self):
        util = Util()
        #PRA PEGAR O VALOR 
        oJson = util.getSymbol('VAR'+str(self.getName()))        
        value = 0#oJson['VALOR']

        if value:
            return value
        else:
            return self.getDefaultValue()

    def getDefaultValue(self):
        return {
            int : 0,
            str : '',
            bool : False,
            float : 0.0,
            object : None
        }[self.type]

