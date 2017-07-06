from util import Util
class Bloco:

    def __init__(self, comando=None):
        self.comando = comando
        self.semantico()

    def __str__(self):
        aux = "<BLOCO> \n"

        if self.comando:
            aux += self.comando.__repr__()
        
        aux += "</BLOCO> \n"
        return aux

    def __repr__(self):
        return self.__str__()

    def semantico(self):
        util = Util()

        if self.comando:
            if not self.comando.semantico():
                return False

        return True