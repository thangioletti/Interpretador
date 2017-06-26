class Program:

    def __init__(self, function=None):
        self.function = function

    def __str__(self):
        aux = "<PROGRAM> \n"
        
        if self.function:
            aux += self.function.__repr__()
            
        aux += "</PROGRAM> \n"
        return aux

    def __repr__(self):
        return self.__str__()