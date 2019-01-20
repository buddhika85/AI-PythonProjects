import numpy as np
import random as rd
from operator import attrgetter
from .ArtificalChomosome import ArtificialChromosomeForBraninRcos
from .BraninRcosObjectiveFunction import BraninRcos
from .PopulationDetails import Population

class ES:
    # initial population
    def CreateInitialPopulation(self, numberOfParents, x1, x2, sigmaX1, sigmaX2):
        initialPopulation = []
        for parentNumber in range(0, numberOfParents):
            randomx1 = np.random.uniform(-5, 10)
            randomx2 = np.random.uniform(0, 15)
            sigmaX1ForGeneration = sigmaX1
            sigmaX21ForGeneration = sigmaX2
            result = BraninRcos().CalculateBraninRcos(randomx1, randomx2)
            artificalChormosome = ArtificialChromosomeForBraninRcos(randomx1, sigmaX1ForGeneration, randomx2,
                                                                    sigmaX21ForGeneration, result)
            initialPopulation.append(artificalChormosome)
        return initialPopulation

    # generations after first generation
    def CreatePopulation(self, parentPopulation, numberOfParents, numberOfChildren, sigmaX1, sigmaX2, OneOverFiveSigmaRuleConstantA):
        childPopulation = []
        oneFifthChildBetterTracker = 0
        for childNumber in range(0, numberOfChildren):
            randomParent = rd.SystemRandom().choice(parentPopulation)  # get random parent
            #print("\nRandom parent")
            #randomParent.DisplayChromosome();
            childX1 = randomParent.x1 + sigmaX1 * np.random.normal(0, 1)
            childX2 = randomParent.x2 + sigmaX2 * np.random.normal(0, 1)
            childResult = BraninRcos().CalculateBraninRcos(childX1, childX2)
            childChormosome = ArtificialChromosomeForBraninRcos(childX1, sigmaX1, childX2, sigmaX2, childResult)
            childPopulation.append(childChormosome)
            # 1/5th Tracker
            if childChormosome.objectiveFunctionResult < randomParent.objectiveFunctionResult:
                oneFifthChildBetterTracker += 1
        # apply 1/5th Rule
        if oneFifthChildBetterTracker > numberOfParents / 5:
            sigmaX1 = sigmaX1 + sigmaX1 * OneOverFiveSigmaRuleConstantA
            sigmaX2 = sigmaX2 + sigmaX2 * OneOverFiveSigmaRuleConstantA
        elif oneFifthChildBetterTracker < numberOfParents / 5:
            sigmaX1 = sigmaX1 - sigmaX1 * OneOverFiveSigmaRuleConstantA
            sigmaX2 = sigmaX2 - sigmaX2 * OneOverFiveSigmaRuleConstantA
        # take best as parents
        childPopulation.sort(key = attrgetter('objectiveFunctionResult'), reverse = False)
        childPopulation = childPopulation[:numberOfParents]
        # return population details
        newPopulation = Population(childPopulation, sigmaX1, sigmaX2)
        return newPopulation

    #get best solution
    def FindBestOfAll(self, generationBestSolutions):
        generationBestSolutions.sort(key = attrgetter('bestOfGeneration.objectiveFunctionResult'), reverse = False)
        best = generationBestSolutions[0]
        return best