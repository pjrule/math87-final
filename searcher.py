import abc


class Searcher(abc.ABC):
    """
    A searcher is someone who is looking for the lost person.
    Just like the lost persons, each searcher may move once in a given turn,
    and his movement is given by the underlying implementation. Searchers
    will likely rely upon some model of how the lost person
    is moving in order to make decisions.
    """

    @abc.abstractmethod
    def get_next(self, scenario_map, current):
        """
        Computes the next location where the searcher will move.
        :param scenario_map: the scenario map
        :param current: the searcher's current location.
        :return: the new location for the searcher after moving.
        """
        raise NotImplementedError('Should be implemented by subclasses')
