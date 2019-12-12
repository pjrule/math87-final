import unittest
from maps.basic_map import BasicMap
from person.stationary_lost_person import StationaryLostPerson
from person.stationary_searcher import StationarySearcher


class BasicMapTest(unittest.TestCase):
    def test_simple(self):
        print('Starting simple test')

        # Create a basic 10x10 map
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

        m.move_lost_person((2, 5), (3, 5))
        m.move_searcher((0, 0), (1, 0))
        m.print()
        self.assertTrue(m.contains_searcher_global((1, 0)))
        self.assertTrue(m.contains_lost_person_global((3, 5)))
        self.assertFalse(m.contains_searcher_global((3, 5)))
        self.assertFalse(m.contains_lost_person_global((2, 5)))


if __name__ == '__main__':
    unittest.main()
