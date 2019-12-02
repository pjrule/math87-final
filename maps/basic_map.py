from maps.map import Map
import networkx as nx


NUM_LPS = 'num_lost_persons'
NUM_SEARCHERS = 'num_searchers'


class BasicMap(Map):
    """
    In the 'Basic Map', all terrain is weighted equally, and visibility is constant
    no matter where you are on the map. There must be at least one lost person
    and one searcher.

    The underlying graph is a grid graph backed by the NetworkX library.
    """
    def __init__(self, rows, cols):
        """Instantiates a Basic Map.

        :param rows: number of rows (must be >= 1)
        :param cols: number of columns (must be >= 1)
        """
        # Validation.
        if rows < 1:
            raise ValueError('Number of rows must be at least 1')
        if cols < 1:
            raise ValueError('Number of columns must be at least 1')

        # Create the graph.
        # Nodes are tuples (e.g. (1,0))
        self.graph = nx.grid_graph(dim=[rows, cols])
        self.rows = rows
        self.cols = cols
        for node in self.graph.nodes:
            self.graph.nodes[node][NUM_LPS] = 0
            self.graph.nodes[node][NUM_SEARCHERS] = 0

    def get_cost(self, v1, v2):
        # Zero cost to move anywhere on the simple map.
        return 0

    def get_visibility(self, v):
        # Can only see neighboring nodes.
        l = list(self.graph.adj[v])
        l.append(v)
        return l

    def contains_lost_person_global(self, v):
        return self.graph.nodes[v][NUM_LPS] > 0

    def contains_lost_person(self, v, current_location):
        return self.contains_lost_person_global(v) and \
            v in self.get_visibility(current_location)

    def contains_searcher_global(self, v):
        return self.graph.nodes[v][NUM_SEARCHERS] > 0

    def contains_searcher(self, v, current_location):
        return self.contains_searcher_global(v) and \
            v in self.get_visibility(current_location)

    def move_lost_person(self, start, end):
        if self.graph.nodes[start][NUM_LPS] <= 0:
            print('No lost person at this start location')
            return False
        if end not in self.get_visibility(start):
            print('Cannot travel greater than max visibility in one time step')
            return False
        # Now move the lost person
        self.graph.nodes[start][NUM_LPS] -= 1
        self.graph.nodes[end][NUM_LPS] += 1

    def move_searcher(self, start, end):
        if self.graph.nodes[start][NUM_SEARCHERS] <= 0:
            print('No searcher at this start location')
            return False
        if end not in self.get_visibility(start):
            print('Cannot travel greater than max visibility in one time step')
            return False
        # Now move the searcher
        self.graph.nodes[start][NUM_SEARCHERS] -= 1
        self.graph.nodes[end][NUM_SEARCHERS] += 1

    def spawn_lost_person(self, start):
        self.graph.nodes[start][NUM_LPS] += 1

    def spawn_searcher(self, start):
        self.graph.nodes[start][NUM_SEARCHERS] += 1

    def recover_lost_person(self, v):
        if self.graph.nodes[v][NUM_LPS] <= 0:
            print('No lost person at this location to recover')
            return False
        else:
            self.graph.nodes[v][NUM_LPS] -= 1

    def print(self):
        print(len(self.graph.nodes))
        for node in self.graph.nodes:
            num_lps = self.graph.nodes[node][NUM_LPS]
            num_searchers = self.graph.nodes[node][NUM_SEARCHERS]
            print(str(node) + ': L = ' + str(num_lps) + ", S = " + str(num_searchers))

    def numRows(self):
        return self.rows

    def numColumns(self):
        return self.cols


