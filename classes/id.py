class Id:

    def __init__(self, value=None):
        self.value = value
        self.type = self.setType()        

    def __str__(self):
        aux = "<ID> \n"

        if self.value:
            aux += self.value + "\n"
        
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
        }[self.value[0]]
        
    def getValue(self):
        return self.value

    def getType(self):
        return self.type

