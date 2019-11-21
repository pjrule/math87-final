import abc


class Map(abc.ABC):
    """
    The Map is a bounded, discrete, two dimensional world that serves
    as a setting for simulating search-and-rescue missions.
    """

    @abc.abstractmethod
    def get_cost(self, v1, v2):
        """
        Get the cost associated with moving along an edge given by (v1, v2).
        :param v1: An identifier for src vertex
        :param v2: An identifier for dest vertex
        :return: The cost
        """
        raise NotImplementedError('Should be implemented by subclasses')

    @abc.abstractmethod
    def get_visibility(self, v):
        """
        Get the visibility range associated with a specific location.
        :param v: a location on the map, likely a user's current location.
        :return: a list of locations that the user can see, represented
        as vertices.
        """
        raise NotImplementedError('Should be implemented by subclasses')

    @abc.abstractmethod
    def contains_lost_person_global(self, v):
        """
        Returns true if location 'v' contains a lost person, false
        otherwise.
        :param v: the location where a lost person could be
        :return: true if location 'v' contains a lost person, false
        otherwise.
        """
        raise NotImplementedError('Should be implemented by subclasses')

    @abc.abstractmethod
    def contains_lost_person(self, v, current_location):
        """
        Returns true if location 'v' contains a lost person AND
        is visible from the current vantage point, false otherwise.
        :param v: the location where a lost person could be
        :param current_location: location of a person looking
        :return: true if location 'v' contains a lost person AND
        is visible from the current vantage point, false otherwise.
        """
        raise NotImplementedError('Should be implemented by subclasses')

    @abc.abstractmethod
    def contains_searcher_global(self, v):
        """
        Returns true if location 'v' contains a searcher, false
        otherwise.
        :param v: the location where a searcher could be
        :return: true if location 'v' contains a searcher, false
        otherwise.
        """
        raise NotImplementedError('Should be implemented by subclasses')

    @abc.abstractmethod
    def contains_searcher(self, v):
        """
        Returns true if location 'v' contains a searcher AND
        is visible from the current vantage point.
        :param v: the location where a searcher could be
        :return: true if location 'v' contains a searcher AND
        is visible from the current vantage point, false otherwise.
        """
        raise NotImplementedError('Should be implemented by subclasses')
