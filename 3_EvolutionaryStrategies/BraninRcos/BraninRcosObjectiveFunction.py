import math as mt

class BraninRcos:
    def __init__(self):
        self.Description = 'This class implements Branin Rcos'

    def CalculateBraninRcos(self, x1, x2):
        x1 = int(x1)
        x2 = int(x2)
        result = ((x2 - ((5.1/(4*mt.pi**2))*x1**2) +
            ((5/mt.pi)*x1) - 6)**2 + 10*(1-(1/(8*mt.pi)))*mt.cos(x1) + 10)
        return result