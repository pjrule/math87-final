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

    def __init__(self, scenario_map, lost_persons, searchers, latency = 10):
        self.scenario_map = scenario_map
        self.lost_persons = lost_persons
        self.searchers = searchers
        self.num_rescued = 0
        self.latency = latency

    def add_latency(self):
        for i in range(self.latency):
            for lost_person in self.lost_persons:
                lost_person.move()

    def simulate(self, num_steps, viewing_mode=ViewingMode.NONE, shortest_path = False):
        """
        Runs the scenario.
        :param num_steps: The number of discrete time steps, or turns.
        :param viewing_mode: The preferred viewing mode.
        :return: Percentage of lost persons found
        """
        # To add latency
        if not shortest_path:
            self.add_latency()

        count = 0
        for i in range(0, num_steps):
            # print('Step: ' + str(i))
            for lost_person in self.lost_persons:
                lost_person.move()

            # Before the searchers move, see if any lost persons
            # have moved into visible range.
            for searcher in self.searchers:
                self.num_rescued += searcher.check_for_lost_persons()

            if self.num_rescued == len(self.lost_persons):
                #print('Mission accomplished!')
                break

            for searcher in self.searchers:
                searcher.move()

            # After moving the searchers, see if any lost persons
            # have become visible.
            for searcher in self.searchers:
                self.num_rescued += searcher.check_for_lost_persons()

            if self.num_rescued == len(self.lost_persons):
                print('Mission accomplished!')
                count += 1
                break

            count += 1
        print('*** Scenario finished. Num iterations: %d, Rescued: %d/%d' % (count, self.num_rescued, len(self.lost_persons)))
        return count
