import unittest
from maps.basic_map import BasicMap
from scenario import Scenario
from person.stationary_lost_person import StationaryLostPerson
from person.stationary_searcher import StationarySearcher


class ScenarioTest(unittest.TestCase):
    def test_scenario_noneFound(self):
        m = BasicMap(10, 10)

        # Add some lost persons to the map
        lp00 = StationaryLostPerson(m)
        lp00.init((2, 5))
        lp01 = StationaryLostPerson(m)
        lp01.init((4, 7))

        # Add some searchers to the map
        searcher00 = StationarySearcher(m)
        searcher00.init((0, 0))
        searcher01 = StationarySearcher(m)
        searcher01.init((0, 0))  # people can be started in the same place

        s = Scenario(m, [lp00, lp01], [searcher00, searcher01])
        s.simulate(10)  # Simulate for ten time steps

    def test_scenario_someFound(self):
        m = BasicMap(10, 10)

        # Add some lost persons to the map
        lp00 = StationaryLostPerson(m)
        lp00.init((2, 5))
        lp01 = StationaryLostPerson(m)
        lp01.init((4, 7))

        # Add some searchers to the map
        searcher00 = StationarySearcher(m)
        searcher00.init((0, 0))
        searcher01 = StationarySearcher(m)
        searcher01.init((2, 5))

        s = Scenario(m, [lp00, lp01], [searcher00, searcher01])
        s.simulate(10)  # Simulate for ten time steps


    def test_scenario_allFound(self):
        m = BasicMap(10, 10)

        # Add some lost persons to the map
        lp00 = StationaryLostPerson(m)
        lp00.init((2, 5))
        lp01 = StationaryLostPerson(m)
        lp01.init((4, 7))

        # Add some searchers to the map
        searcher00 = StationarySearcher(m)
        searcher00.init((4, 8))
        searcher01 = StationarySearcher(m)
        searcher01.init((3, 5))

        s = Scenario(m, [lp00, lp01], [searcher00, searcher01])
        s.simulate(10)  # Simulate for ten time steps


if __name__ == '__main__':
    unittest.main()