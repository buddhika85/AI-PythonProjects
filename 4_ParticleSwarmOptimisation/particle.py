class Particle:
    global_best_position = [0, 0]
    global_best_cost = float("inf")

    def __init__(self, particle_Number, current_position, current_cost,
                 personal_best_position, personal_best_cost):
        self.particle_Number = particle_Number
        self.current_position = current_position
        self.current_cost = current_cost
        self.personal_best_position = personal_best_position
        self.personal_best_cost = personal_best_cost

    def __str__(self):
        return str(f"Particle Number => {self.particle_Number} \n"
              f"Current Position [{self.current_position[0]}, {self.current_position[1]}] \n"
              f"Personal Best [{self.personal_best_position[0]}, {self.personal_best_position[1]}] "
              f"=> {self.personal_best_cost} \n"
              f"Global Best [{Particle.global_best_position[0]}, {Particle.global_best_position[1]}] "
              f"=> {Particle.global_best_cost}\n")
