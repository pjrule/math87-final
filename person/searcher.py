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
    def init(self, start):
        """
        Move the person to his starting location
        :param start: the starting location on the map (a tuple)
        :return:
        """
        raise NotImplementedError('Should be implemented by subclasses')

    @abc.abstractmethod
    def move(self):
        """
        Give the person an opportunity to move to a new space
        on the map.
        :return:
        """
        raise NotImplementedError('Should be implemented by subclasses')

    @abc.abstractmethod
    def check_for_lost_persons(self):
        """
        Look for lost persons for current location.
        :return: True if lost person located, false otherwise
        """
        raise NotImplementedError('Should be implemented by subclasses')

    @abc.abstractmethod
    def get_history(self):
        """
        Gets a list of locations at which this person was located, ordered
        by time visited.
        :return: ordered list of visited locations
        """
        raise NotImplementedError('Should be implemented by subclasses')
