class Id:

    def __init__(self, value=None):
        self.value = value

    def __str__(self):
        aux = "<ID> \n"

        if self.value:
            aux += self.value + "\n"
        
        aux = "</ID> \n"
        return aux
    
    def __repr__(self):
        return self.__str__()