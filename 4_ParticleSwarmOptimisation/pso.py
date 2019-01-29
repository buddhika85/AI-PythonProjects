import numpy as np
import random

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
            # current_velocity = 0
            particle = Particle(particleNumber + 1, [random_x1, random_x2], current_cost, [0, 0],
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
    def run_particle_swarm_optimisation(self, initial_swarm, config: Configurations):
        # starting from second iteration and running all iterations after
        swarm = initial_swarm   # for the 2nd Iter
        for iterationNumber in range(1, config.iterations):
            branin_rcos_objective_function: BraninRcos = BraninRcos()
            for particleNumber in range(0, len(swarm)):
                # x1
                x1 = swarm[particleNumber].current_position[0]
                x1_velocity = swarm[particleNumber].current_velocity[0]
                x1_personal_best = swarm[particleNumber].personal_best_position[0]
                x1_global_best = Particle.global_best_position[0]
                new_position_velocity = self.calculate_new_position(x1, x1_velocity, x1_personal_best, x1_global_best,
                                                                    config, config.x1_min, config.x1_max)
                swarm[particleNumber].current_position[0] = new_position_velocity[0]
                swarm[particleNumber].current_velocity[0] =  new_position_velocity[1]
                # x2
                x2 = swarm[particleNumber].current_position[1]
                x2_velocity = swarm[particleNumber].current_velocity[1]
                x2_personal_best = swarm[particleNumber].personal_best_position[1]
                x2_global_best = Particle.global_best_position[1]
                new_position_velocity = self.calculate_new_position(x2, x2_velocity, x2_personal_best, x2_global_best,
                                                                    config, config.x2_min, config.x2_max)
                swarm[particleNumber].current_position[1] = new_position_velocity[0]
                swarm[particleNumber].current_velocity[1] = new_position_velocity[1]
                swarm[particleNumber].current_cost = branin_rcos_objective_function.CalculateBraninRcos(
                    swarm[particleNumber].current_position[0], swarm[particleNumber].current_position[1])
                # personal best
                if swarm[particleNumber].personal_best_cost > swarm[particleNumber].current_cost:
                    swarm[particleNumber].personal_best_position = [swarm[particleNumber].current_position[0],
                                                                    swarm[particleNumber].current_position[1]]
                    swarm[particleNumber].personal_best_cost = swarm[particleNumber].current_cost
                # global best
                if Particle.global_best_cost > swarm[particleNumber].current_cost:
                    Particle.global_best_position = [swarm[particleNumber].current_position[0],
                                                                    swarm[particleNumber].current_position[1]]
                    Particle.global_best_cost = swarm[particleNumber].current_cost
                print(f"Iteration {iterationNumber + 1}'s Particle {particleNumber + 1} done")
            # with each iteration w gets decreased
            config.w_inertia_weight = config.w_inertia_weight * config.w_damping
            print (f"Iteration {iterationNumber + 1} done")
        return swarm


    # displays the swarm
    def display_swarm(self, swarm):
        for particleNumber in range(0, len(swarm)):
            print(swarm[particleNumber])

    # new position
    def calculate_new_position_check(self, current_position, current_velocity, current_personal_best, current_global_best, config: Configurations, lower_bound, upper_bound) -> float:
        do_again = True
        new_velocity = 0
        new_position = 0
        r1_random = random.uniform(0, 1)
        r2_random = random.uniform(0, 1)
        new_velocity = (config.w_inertia_weight * current_velocity) + \
                       (r1_random * config.c1_cognitive_weight * (current_personal_best - current_position)) + \
                       (r2_random * config.c2_social_weight * (current_global_best - current_position))
        new_position = current_position + new_velocity
        return [new_position, new_velocity]

    # new position
    def calculate_new_position(self, current_position, current_velocity, current_personal_best, current_global_best,
                               config: Configurations, lower_bound, upper_bound) -> float:
        do_again = True
        new_velocity = 0
        new_position = 0
        while (do_again):
            r1_random = random.uniform(0, 1)
            r2_random = random.uniform(0, 1)
            new_velocity = ((config.w_inertia_weight * current_velocity) +
                            (r1_random * config.c1_cognitive_weight * (current_personal_best - current_position)) +
                            (r2_random * config.c2_social_weight * (current_global_best - current_position)))
            new_position = current_position + new_velocity
            if new_position < lower_bound or new_position > upper_bound:
                do_again = True
                # below will reduce time to get values with in lower and upper bounds
                if new_position > upper_bound:
                    current_velocity = current_velocity * 0.9
                    print (current_velocity)
                if new_position < lower_bound:
                    current_velocity = current_velocity * 1.1
                    print(current_velocity)
            else:
                do_again = False
            if (current_velocity == float("-inf")):
                print ("minus inifinity")
            if (current_velocity == float("inf")):
                print ("positive inifinity")
        return [new_position, new_velocity]



