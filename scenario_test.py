import unittest
from maps.basic_map import BasicMap
from scenario import Scenario
from person.stationary_lost_person import StationaryLostPerson
from person.stationary_searcher import StationarySearcher
from person.random_walk_lost_person import RandomWalkLostPerson
from person.shortest_path_lost_person import ShortestPathLostPerson
from person.random_walk_searcher import RandomWalkSearcher
from maps.quadrant_partitioner import QuadrantPartitioner


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

        s = Scenario(m, [lp00], [searcher00], True)
        s.simulate(100)  # Simulate for N time steps
        print(lp00.get_history())
        print(searcher00.get_history())

    def test_scenario_one_random_searcher(self):
        m = BasicMap(15, 15)

        middle = (7,7)

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


    def test_scenario_one_multiple_searcher(self):
        m = BasicMap(15, 15)

        middle = (7,7)

        # Add some lost persons to the map
        lp00 = RandomWalkLostPerson(m)
        lp00.init(middle)

        searchers = []


        for i in range(10):
            # Add some searchers to the map
            searcher = RandomWalkSearcher(m)
            searcher.init(middle)
            searchers.append(searcher)


        s = Scenario(m, [lp00], searchers)
        s.simulate(100)  # Simulate for N time steps
        print("lost person history: \n")
        print(lp00.get_history())
        print("\n")
        for i in range(10):
            print("searcher history: " , i)
            print(searchers[i].get_history())
            print("\n")


    def test_quadrant_partitioner(self):
        m = BasicMap(15, 15)

        middle = (7,7)

        # Add some lost persons to the map
        lp00 = RandomWalkLostPerson(m)
        lp00.init(middle)

        # Partition map into quadrants
        searchers = []

        partitioner = QuadrantPartitioner()
        [rows_midpoint, cols_midpoint] = partitioner.partition(m)
        quad01_rows = (0, rows_midpoint)
        quad01_cols = (0, cols_midpoint)
        s00 = RandomWalkSearcher(m, quad01_rows, quad01_cols)
        s00.init(middle)
        searchers.append(s00)

        quad02_rows = (0, rows_midpoint)
        quad02_cols = (cols_midpoint, m.numColumns()-1)
        s01 = RandomWalkSearcher(m, quad02_rows, quad02_cols)
        s01.init(middle)
        searchers.append(s01)

        quad03_rows = (rows_midpoint, m.numRows()-1)
        quad03_cols = (0, cols_midpoint-1)
        s02 = RandomWalkSearcher(m, quad03_rows, quad03_cols)
        s02.init(middle)
        searchers.append(s02)

        quad04_rows = (rows_midpoint, m.numRows()-1)
        quad04_cols = (cols_midpoint, m.numColumns()-1)
        s03 = RandomWalkSearcher(m, quad04_rows, quad04_cols)
        s03.init(middle)
        searchers.append(s03)

        scenario = Scenario(m, [lp00], searchers)
        scenario.simulate(100)

        print("lost person history: \n")
        print(lp00.get_history())
        print("\n")
        for i in range(4):
            print("searcher history: " , i)
            print(searchers[i].get_history())
            print("\n")


if __name__ == '__main__':
    unittest.main()