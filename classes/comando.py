from util import Util
class Comando:

    def __init__(self, comando1=None, comando2=None):
        self.comando1 = comando1
        self.comando2 = comando2        

    def __str__(self):
        aux = "<COMANDO> \n"

        if self.comando1:
            aux += self.comando1.__repr__()
        
        if self.comando2:
            aux += self.comando2.__repr__()

        aux += "</COMANDO> \n"
        return aux

    def __repr__(self):
        return self.__str__()    

    def semantico(self):
        util = Util()

        if self.comando1:
            if not self.comando1.semantico():
                return False
        
        if self.comando2:
            if not self.comando2.semantico():
                return False
        
        return True