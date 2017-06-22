# expression = (expression)
#
class Factor:

    def __init__(self, id=None, number=None, expression=None):
        self.id=id
        self.number=number
        self.expression=expression

    def __str__(self):
        aux = "<FACTOR> \n"

        if (self.expression):
             aux += "( \n"
             aux += self.expression
             aux += ") \n"
        
        if self.id:
            aux += self.id
        elif self.number:
            aux += str(self.number) + "\n"
        
        aux += "</FACTOR> \n"
        return aux

    def __repr__(self):
        return self.__str__()