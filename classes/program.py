from util import Util
class Program:

    def __init__(self, function=None):
        self.function = function
        self.semantico()

    def __str__(self):
        aux = "<PROGRAM> \n"
        
        if self.function:
            aux += self.function.__repr__()
            
        aux += "</PROGRAM> \n"
        return aux

    def __repr__(self):
        return self.__str__()

    def semantico(self):
        if self.function:
            if not self.function.semantico():
                return False

        return True
    