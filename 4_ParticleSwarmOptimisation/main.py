from pso import ParticleSwarmOptimizer
from config import Configurations


class Program:

    def main(self):
        print("\nDemo finding minimal output combinations for Branin Rcos")
        config = Configurations()
        pso = ParticleSwarmOptimizer()
        # first iteration
        print("\nFirst iterations swarm")
        initial_swarm = pso.create_initial_swarm(config)
        pso.display_swarm(initial_swarm)
        # iteration 2 onwards
        final_swarm = pso.run_particle_swarm_optimisation(initial_swarm, config)
        print("\nFinal iterations swarm")
        pso.display_swarm(final_swarm)

Program().main()
