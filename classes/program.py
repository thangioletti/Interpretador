from util import Util
class Program:

    def __init__(self, bloco=None):
        self.bloco = bloco
        self.semantico()

    def __str__(self):
        aux = "<PROGRAM> \n"
        
        if self.bloco:
            aux += self.bloco.__repr__()
            
        aux += "</PROGRAM> \n"
        return aux

    def __repr__(self):
        return self.__str__()

    def semantico(self):
        if self.bloco:
            if not self.bloco.semantico():
                return False

        return True
    