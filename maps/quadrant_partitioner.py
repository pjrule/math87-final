from maps.partitioner import Partitioner
import math


class QuadrantPartitioner(Partitioner):
    def partition(self, scenario_map):
        num_rows = scenario_map.numRows()
        num_cols = scenario_map.numColumns()
        rows_midpoint = math.floor(num_rows / 2)
        cols_midpoint = math.floor(num_cols / 2)
        return rows_midpoint, cols_midpoint
