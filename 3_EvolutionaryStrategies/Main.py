
from BraninRcos.BraninRcosObjectiveFunction import BraninRcos
from BraninRcos.Config import Configurations
from BraninRcos.EvolutionaryStrategy import ES
from BraninRcos.GenerationDetails import Generation
from BraninRcos.ArtificalChomosome import ArtificialChromosomeForBraninRcos

class Program:

    @staticmethod
    def Main():
        print('\nDemonstrates the usage of Evolutionary Strategies to Solve Branin Rcos function')
        config = Configurations();
        braninRcos = BraninRcos()
        result = braninRcos.CalculateBraninRcos(config.x1, config.x2)
        print(f"Initial Test Result\nx1 = {config.x1}, x2 = {config.x2}, result = {result}\n")

        # create initial population
        es = ES()
        initialPopulation = es.CreateInitialPopulation(config.numberOfParentsMiu, config.x1, config.x2, config.sigmaX1,
                                                       config.sigmaX2)
        #print("\nFirst Generation")
        #Program.DisplayPopulation(initialPopulation)

        #store best solution of initial population
        generationBestSolutions = []
        best = Program.GetBestOfGeneration(initialPopulation, 1)
        generationBestSolutions.append(best)
        print("\nBest of First Generation")
        best.bestOfGeneration.DisplayChromosome()

        #create generations after the first generation
        parentPopulation = []
        for generationNumber in range(2, config.numberOfGenerationsM + 1):
            if generationNumber == 2:
                parentPopulation = es.CreatePopulation(initialPopulation, config.numberOfParentsMiu,
                                                       config.numberOfChildrenLambda, config.sigmaX1, config.sigmaX2,
                                                       config.OneOverFiveSigmaRuleConstantA)
            else:
                parentPopulation = es.CreatePopulation(parentPopulation.species, config.numberOfParentsMiu,
                                                       config.numberOfChildrenLambda, parentPopulation.sigmaX1ForNext, parentPopulation.sigmaX2ForNext,
                                                       config.OneOverFiveSigmaRuleConstantA)
            best = Program.GetBestOfGeneration(parentPopulation.species, generationNumber)
            #Program.DisplayPopulation(parentPopulation.species)
            generationBestSolutions.append(best)
            print(f"\nBest of Generation {generationNumber}")
            best.bestOfGeneration.DisplayChromosome()

        # find best of all generations and display
        bestOfAll = es.FindBestOfAll(generationBestSolutions)
        print(f"\nBest of ES Run - Generation Number {bestOfAll.generationNumber}")
        bestOfAll.bestOfGeneration.DisplayChromosome()

    @staticmethod
    def DisplayPopulation(population):
        for parent in population:
            parent.DisplayChromosome()

    @staticmethod
    def GetBestOfGeneration(population, generationNumber):
        bestChromosomeOfGeneration = ArtificialChromosomeForBraninRcos(0, 0, 0, 0, 0)
        bestChromosomeOfGeneration.objectiveFunctionResult = float("inf")
        best = Generation(0, bestChromosomeOfGeneration)
        for parentNumber in range(0, len(population)):
            if population[parentNumber].objectiveFunctionResult <= best.bestOfGeneration.objectiveFunctionResult:
                best.bestOfGeneration = population[parentNumber]
                best.generationNumber = generationNumber
        return best;



Program.Main()
