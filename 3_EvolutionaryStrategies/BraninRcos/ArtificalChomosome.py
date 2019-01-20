class ArtificialChromosomeForBraninRcos:

    def __init__(self, x1, sigmaX1, x2, sigmaX2, objectiveFunctionResult):
        self.x1 = x1
        self.sigmaX1 = sigmaX1
        self.x2 = x2
        self.sigmaX2 = sigmaX2
        self.objectiveFunctionResult = objectiveFunctionResult

    def DisplayChromosome(self):
        print(f"x1 = {self.x1} | sigmaX1 = {self.sigmaX1} | x2 = {self.x2} | sigmax2 = {self.sigmaX2} | result = {self.objectiveFunctionResult}")

