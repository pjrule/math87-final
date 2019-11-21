from enum import Enum


class ViewingMode(Enum):
    # No visual output
    NONE = 1
    # Turn-based animation of searchers and lost persons moving around
    # on the map.
    GLOBAL = 2
    # Turn-based animation of lost persons only.
    LOST_PERSON = 3
    # Turn-based animation of searchers, along with the probability
    # distributions being used to model the lost persons.
    SEARCHER = 4


class Scenario:
    """
    A Scenario represents a search-and-rescue operation.
    It consists of:
    - A map, possibly with elevation-based edge weights
    - At least one lost person
    - At least one searcher
    Scenarios last for a finite amount of time. In addition, time is
    assumed to be discrete. All lost persons and searchers on the map
    are provided with the opportunity to move at each discrete time
    step, or 'turn'.
    """

    def __init__(self, scenario_map, lost_persons, searchers):
        self.scenario_map = scenario_map
        self.lost_persons = lost_persons
        self.searchers = searchers

    def simulate(self, num_steps, viewing_mode):
        """
        Runs the scenario.
        :param num_steps: The number of discrete time steps, or turns.
        :param viewing_mode: The preferred viewing mode.
        :return: Percentage of lost persons found
        """
        raise NotImplementedError("Not yet implemented")
