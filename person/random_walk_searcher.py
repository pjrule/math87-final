from person import searcher
import random


class RandomWalkSearcher(searcher.Searcher):
	"""
    A searcher who moves randomly within a bounded area
    """

	def __init__(self, scenario_map, row_range=None, col_range=None):
		self.scenario_map = scenario_map
		self.history = []
		if row_range is None:
			self.row_range = (0, self.scenario_map.numRows() - 1)
		else:
			self.row_range = row_range
		if col_range is None:
			self.col_range = (0, self.scenario_map.numColumns() - 1)
		else:
			self.col_range = col_range

	def init(self, start):
		self.current = start
		self.scenario_map.spawn_searcher(start)
		self.history.append(self.current)

	def move(self):
		# Can move up, down, left, right, or remain stationary with
		# equal probability (1/5)
		choice = random.randint(1, 5)
		old_location = self.current
		new_location = list(self.current)
		if choice == 1:  # UP
			if self.current[0] > self.row_range[0]:
				new_location[0] -= 1
		elif choice == 2:  # DOWN
			if self.current[0] < self.row_range[1]:
				new_location[0] += 1
		elif choice == 3:  # LEFT
			if self.current[1] > self.col_range[0]:
				new_location[1] -= 1
		elif choice == 4:  # RIGHT
			if self.current[1] < self.col_range[1]:
				new_location[1] += 1
		self.current = tuple(new_location)
		self.history.append(self.current)

		## Added this to update the board
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
