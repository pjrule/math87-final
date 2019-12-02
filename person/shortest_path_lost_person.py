from person import lostperson


class ShortestPathLostPerson(lostperson.LostPerson):
    def __init__(self, scenario_map, destination):
        """
        :param scenario_map:
        :param destination: a tuple indicating where the lost person is trying to go.
        """
        self.scenario_map = scenario_map
        self.current = None
        self.index = 0
        self.history = []
        self.path = []
        self.destination = destination

    def init(self, start):
        self.scenario_map.spawn_lost_person(start)
        self.current = start
        self.history.append(start)
        # Compute shortest path to destination
        self.path = self.scenario_map.get_shortest_path(start, self.destination)

    def move(self):
        if self.index < len(self.path):
            self.index += 1
            prev = self.current
            self.current = self.path[self.index]
            self.scenario_map.move_lost_person(prev, self.current)
            self.history.append(self.current)

    def get_history(self):
        return self.history