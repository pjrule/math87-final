"""Estimation of the distribution of a walker's location over time."""
import numpy as np
from copy import deepcopy

class GridDistribution:
    """A time-dependent empirical probability distribution."""
    def __init__(self, walker, scenario_map, n_steps, n_walkers=300):
        # START HACK! (in refactor, scenario_map shouldn't be stored w/in walkers for this reason)
        walker.scenario_map = None
        self.walkers = [deepcopy(walker) for _ in range(n_walkers)]
        walker.scenario_map = scenario_map   
        for walker in self.walkers:
            walker.scenario_map = scenario_map
        # END HACK
        self.dist = np.zeros((n_steps, scenario_map.rows, scenario_map.cols))
        self.scenario_map = scenario_map
        self.n_steps = n_steps
        self.n_walkers = n_walkers

    def run(self):
        """Runs a Monte Carlo simulation to approximate the distribution."""
        for walker in self.walkers:
            self.scenario_map.spawn_lost_person(walker.current)
        for step_idx in range(self.n_steps):
            for walker in self.walkers:
                x = walker.current[0]
                y = walker.current[1]
                self.dist[step_idx, x, y] += 1
                old_location = walker.current
                walker.move()

    def at_step(self, step_idx):
        """Returns the estimated probability distribution at a step.

        :param step_idx: The 0-indexed step to return the distribution for.
            In general, the distribution will become more diffuse over time
            for a random walk.
        :return: An empirical probability distribution in matrix form, with the
            dimension of the matrix corresponding to the dimension of the map
            (a grid).
        """
        return self.dist[step_idx] / self.dist[step_idx].sum()

def expected_reward(dist, x, y):
        """Returns the expected reward at (x, y) with visibility radius 1."""
        adj = {
            (x, y),
            (max(x - 1, 0), y),
            (min(x + 1, dist.shape[0] - 1), y),
            (x, max(y - 1, 0)),
            (x, min(y + 1, dist.shape[1] - 1))
        }
        return sum(dist[adj_x, adj_y] for adj_x, adj_y in adj)