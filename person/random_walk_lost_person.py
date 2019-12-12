from person import lostperson
import random


class RandomWalkLostPerson(lostperson.LostPerson):
    def __init__(self, scenario_map):
        self.scenario_map = scenario_map
        self.history = []
        self.current = None

    def init(self, start):
        self.current = start
        self.scenario_map.spawn_lost_person(start)
        self.history.append(self.current)

    def move(self):
        # Can move up, down, left, right, or remain stationary with
        # equal probability (1/5)
        choice = random.randint(1, 5)
        old_location = self.current
        new_location = list(self.current)
        if choice == 1:  # UP
            if self.current[0] > 0:
                new_location[0] -= 1
        elif choice == 2:  # DOWN
            if self.current[0] < self.scenario_map.numRows()-1:
                new_location[0] += 1
        elif choice == 3:  # LEFT
            if self.current[1] > 0:
                new_location[1] -= 1
        elif choice == 4:  # RIGHT
            if self.current[1] < self.scenario_map.numColumns()-1:
                new_location[1] += 1
        self.current = tuple(new_location)
        self.history.append(self.current)

        ## added this to update scenario map
        self.scenario_map.move_lost_person(old_location, self.current)

    def get_history(self):
        return self.history