from person import searcher
import random


class VerticalSweepSearcher(searcher.Searcher):
    def __init__(self, scenario_map, col_range=None):
        self.scenario_map = scenario_map
        self.history = []
        self.direction = True  # go UP
        if col_range is None:
            self.col_range = (0, self.scenario_map.numColumns() - 1)
        else:
            self.col_range = col_range
        # print(self.col_range)

    def init(self, start):
        self.current = start
        self.scenario_map.spawn_searcher(start)
        self.history.append(self.current)

    def move(self):
        # Can move up, left, or right with equal probability (1/3), until top of
        # map is reached. Then the searchers move down, sweeping back and forth.
        # Change direction if necessary
        if self.direction and self.current[0] == 0:  # Heading up, but at top
            # Move down
            self.direction = False
        elif not self.direction and self.current[0] == self.scenario_map.numRows()-1:
            self.direction = True

        # Make a move!
        old_location = self.current
        new_location = list(self.current)

        if self.current[1] == self.col_range[0]:  # can only move up/down and right
            choice = random.randint(1,2)
            if choice == 2:
                choice = 3
        elif self.current[1] == self.col_range[1]:
            choice = random.randint(1,2)
        else:
            choice = random.randint(1,3)

        if self.direction:  # heading up
            if choice == 1:  # UP
                new_location[0] -= 1
            elif choice == 2:  # LEFT
                new_location[1] -= 1
            elif choice == 3:  # RIGHT
                new_location[1] += 1
        else:  # heading down
            if choice == 1:  # DOWN
                new_location[0] += 1
            elif choice == 2:  # LEFT
                new_location[1] -= 1
            elif choice == 3:  # RIGHT
                new_location[1] += 1

        self.current = tuple(new_location)
        self.history.append(self.current)

        # Added this to update the board
        self.scenario_map.move_searcher(old_location, self.current)

    def check_for_lost_persons(self):
        num_found = 0
        visible_nodes = self.scenario_map.get_visibility(self.current)
        for node in visible_nodes:
            if self.scenario_map.contains_lost_person(node, self.current):
                self.scenario_map.recover_lost_person(node)
                num_found += 1
        return num_found

    def get_history(self):
        return self.history
