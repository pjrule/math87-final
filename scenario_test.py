import unittest
from maps.basic_map import BasicMap
from scenario import Scenario
from person.stationary_lost_person import StationaryLostPerson
from person.stationary_searcher import StationarySearcher
from person.random_walk_lost_person import RandomWalkLostPerson
from person.shortest_path_lost_person import ShortestPathLostPerson
from person.random_walk_searcher import RandomWalkSearcher


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
        s.simulate(10)  # Simulate for N time steps

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
        s.simulate(10)  # Simulate for N time steps


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
        s.simulate(10)  # Simulate for N time steps

    def test_scenario_randomWalker(self):
        m = BasicMap(10, 10)

        # Add some lost persons to the map
        lp00 = RandomWalkLostPerson(m)
        lp00.init((2, 5))

        # Add some searchers to the map
        searcher00 = StationarySearcher(m)
        searcher00.init((4, 8))

        s = Scenario(m, [lp00], [searcher00])
        s.simulate(10)  # Simulate for N time steps
        print(lp00.get_history())
        print(searcher00.get_history())



        # only test that is failing

    def test_scenario_shortestPath(self):
        m = BasicMap(10, 10)

        # Add some lost persons to the map
        lp00 = ShortestPathLostPerson(m, (0, 9))
        lp00.init((2, 5))

        # Add some searchers to the map
        searcher00 = StationarySearcher(m)
        searcher00.init((1, 9))

        s = Scenario(m, [lp00], [searcher00])
        s.simulate(100)  # Simulate for N time steps
        print(lp00.get_history())
        print(searcher00.get_history())

    def test_scenario_one_random_searcher(self):
        m = BasicMap(15, 15)

        middle = (7,8)

        # Add some lost persons to the map
        lp00 = RandomWalkLostPerson(m)
        lp00.init(middle)

        # Add some searchers to the map
        searcher00 = RandomWalkSearcher(m)
        searcher00.init(middle)

        s = Scenario(m, [lp00], [searcher00])
        s.simulate(100)  # Simulate for N time steps
        print("lost person history: \n")
        print(lp00.get_history())
        print("\n")
        print("searcher history: ")
        print(searcher00.get_history())


if __name__ == '__main__':
    unittest.main()