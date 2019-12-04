from person import searcher
import random

class RandomWalkSearcher(searcher.Searcher):
	"""
    A searcher who moves randomly
    """
	def __init__(self, scenario_map):
	    self.scenario_map = scenario_map
	    self.history = []

	def init(self, start):
	    self.current = start
	    self.scenario_map.spawn_searcher(start)
	    self.history.append(self.current)

	def move(self):
		# Can move up, down, left, right, or remain stationary with
		# equal probability (1/5)
		choice = random.randint(1, 6)
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

	def check_for_lost_persons(self):
		num_found = 0
		visible_nodes = self.scenario_map.get_visibility(self.current)
		for node in visible_nodes:
			print(node)
			if self.scenario_map.contains_lost_person(node, self.current):
				self.scenario_map.recover_lost_person(node)
				num_found += 1
		return num_found

	def get_history(self):
		return self.history
        