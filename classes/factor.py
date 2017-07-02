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
             aux += self.expression.__repr__()
             aux += ") \n"
        
        elif self.id:
            aux += self.id.__repr__()
        elif self.number:
            aux += str(self.number) + "\n"
        
        aux += "</FACTOR> \n"
        return aux

    def __repr__(self):
        return self.__str__()

    def getNumber(self):
        return self.number

    def getValue(self):
        if self.expression:
            return self.expression.getValue()
        elif self.id:
            return self.id.getValue()
        else:
            return self.number