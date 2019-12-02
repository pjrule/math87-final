from person import searcher


class StationarySearcher(searcher.Searcher):
    """
    A searcher who never moves. This establishes a baseline against which other
    models can be compared.
    """

    def __init__(self, scenario_map):
        self.scenario_map = scenario_map
        self.history = []

    def init(self, start):
        self.current = start
        self.scenario_map.spawn_searcher(start)

    def move(self):
        self.history.append(self.current)

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