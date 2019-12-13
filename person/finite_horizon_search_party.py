from functools import lru_cache
from collections import deque
from person import searcher
from person.random_walk_lost_person import RandomWalkLostPerson
from person.distribution import GridDistribution, expected_reward

class FiniteHorizonParty:
    """
    A finite-horizon grid search party (for coordinated search).
    """
    def __init__(self, scenario_map, latency, n_searchers, dist, horizon_size=30, max_steps=100):
        self.scenario_map = scenario_map
        self.latency = latency
        self.n_searchers = n_searchers
        self.horizon = horizon_size
        self.paths = []
        self.max_steps = max_steps
        self.dist = dist
        self.t = 0
        self.start = None
        self._tic = 0
        self.current = None

    def init(self, last_seen):
        self.start = tuple(last_seen)
        self.current = [self.start] * self.n_searchers
        
    def get_path(self, searcher_idx):
        return self.paths[searcher_idx]
    
    def tic(self, index, current):
        self.current[index] = current
        self._tic -= 1
    
    def refresh(self):
        if self._tic == 0:
            if self.max_steps - self.t < self.horizon:
                horizon = self.max_steps - self.t
            else:
                horizon = self.horizon
            paths = []
            for idx in range(self.n_searchers):
                paths.append(tuple(best_multipath(tuple(self.current[idx]),
                                                  self.t + self.latency,
                                                  horizon,
                                                  self.dist,
                                                  tuple(paths))))
            self.t += self.horizon    
            self.paths = paths
            self._tic = self.n_searchers * horizon
    
    
class FiniteHorizonPartySearcher(searcher.Searcher):
    """
    A finite-horizon grid searcher.
    """
    def __init__(self, party, index):
        self.party = party
        self.scenario_map = party.scenario_map
        self.index = index
        self._move_buf = deque()
        self.current = None
        self.history = []
        
    def init(self):
        self.scenario_map.spawn_searcher(self.party.start)
        self.current = self.party.start
        self.history.append(self.party.start)
        
    def move(self):
        if not self._move_buf:
            self.party.refresh()
            for move in self.party.get_path(self.index):
                self._move_buf.append(move[0])
        old_location = self.current
        self.current = self._move_buf.popleft()
        self.history.append(self.current)
        self.scenario_map.move_searcher(old_location, self.current)
        self.party.tic(self.index, self.current)

    def check_for_lost_persons(self):
        num_found = 0
        visible_nodes = self.scenario_map.get_visibility(self.current)
        for node in visible_nodes:
            if self.scenario_map.contains_lost_person(node, self.current):
                self.scenario_map.recover_lost_person(node)
                num_found += 1
        return num_found

    def get_history(self):
        return self.history
    
    
@lru_cache(maxsize=2**20)
def best_multipath(loc, t, left, dist, other_paths=None):
    t_dist = dist.at_step(t)
    if other_paths:
        # Mask off all points within the visibility radius
        # (fixed at 1 for this project) of each path.
        for other_path in other_paths:
            t_idx = len(other_path) - left
            other_loc = other_path[t_idx][0]
            for x, y in possible(other_loc, t_dist):
                t_dist[x, y] = 0    
    possible_locs = possible(loc, t_dist)
    rewards = {
        possible_loc: expected_reward(t_dist,
                                      possible_loc[0],
                                      possible_loc[1])
        for possible_loc in possible_locs
    }
    if left == 1:
        return [tuple(sorted(rewards.items(), key=lambda kv: kv[1])[-1])]
    elif left > 1:
        paths = []
        for next_loc in possible_locs:
            best_direction = best_multipath(next_loc, t + 1, left - 1,
                                            dist, other_paths)
            curr_reward = expected_reward(t_dist, next_loc[0], next_loc[1])
            total_reward = curr_reward + sum(s[1] for s in best_direction)
            path = [(next_loc, curr_reward), *best_direction]
            paths.append((path, total_reward))
        return sorted(paths, key=lambda kv: kv[1])[-1][0]
    
    
def possible(loc, t_dist):
    """Returns grid coordinates within a radius of 1."""
    return [
        loc,
        (max(loc[0] - 1, 0), loc[1]),
        (min(loc[0] + 1, t_dist.shape[0] - 1), loc[1]),
        (loc[0], max(loc[1] - 1, 0)),
        (loc[0], min(loc[1] + 1, t_dist.shape[1] - 1))
    ]