import numpy as np

from config import Configurations
from particle import Particle
from BraninRcos import BraninRcos


class ParticleSwarmOptimizer:

    # creates initial swarm
    def create_initial_swarm(self, config: Configurations) -> []:
        swarm_of_Particles = []
        branin_rcos_objective_function: BraninRcos = BraninRcos()
        for particleNumber in range(0, config.particles_per_swarm):
            random_x1 = np.random.uniform(-5, 10)
            random_x2 = np.random.uniform(0, 15)
            current_cost = branin_rcos_objective_function.CalculateBraninRcos(random_x1, random_x2)
            particle = Particle(particleNumber + 1, [random_x1, random_x2], current_cost,
                                [random_x1, random_x2], current_cost)
            swarm_of_Particles.append(particle)
            # global best
            if particleNumber == 0:
                Particle.global_best_position = [random_x1, random_x2]
                Particle.global_best_cost = current_cost
            else:
                if particleNumber > 0 and Particle.global_best_cost > current_cost:
                    Particle.global_best_position = [random_x1, random_x2]
                    Particle.global_best_cost = current_cost
        return swarm_of_Particles

    # run pso
    ##def run_particle_swarm_optimisation(self, config: Configurations, initial_swarm):


    # displays the swarm
    def display_swarm(self, swarm):
        for particleNumber in range(0, len(swarm)):
            print(swarm[particleNumber])
