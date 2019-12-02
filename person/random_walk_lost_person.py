from person import lostperson
import random

class RandomWalkLostPerson(lostperson.LostPerson):
    def __init__(self, scenario_map):
        self.scenario_map = scenario_map
        self.history = []

    def init(self, start):
        self.current = start
        self.scenario_map.spawn_lost_person(start)
        self.history.append(self.current)

    def move(self):
        # Can move up, down, left, right, or remain stationary with
        # equal probability (1/5)
        choice = random.randint(1, 6)
        if choice == 1:  # UP
            pass
        elif choice == 2:  # DOWN
            pass
        elif choice == 3:  # LEFT
            pass
        elif choice == 4:  # RIGHT
            pass
        else:  # STATIONARY
            pass
        self.history.append(self.current)

    def get_history(self):
        return self.history