import lostperson


class StationaryLostPerson(lostperson.LostPerson):
    """
    A lost person who never moves.
    """

    def __init__(self, scenario_map):
        self.scenario_map = scenario_map
        self.history = []

    def init(self, start):
        self.current = start
        self.scenario_map.spawn_lost_person(start)

    def move(self):
        self.history.append(self.current)

    def get_history(self):
        return self.history
