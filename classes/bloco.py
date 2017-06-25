class Bloco:

    def __init__(self, comando=None):
        self.comando = comando

    def __str__(self):
        aux = "<BLOCO> \n"

        if self.comando:
            aux += self.comando.__repr__()
        
        aux += "</BLOCO> \n"
        return aux

    def __repr__(self):
        return self.__str__()