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
    def contains_searcher(self, v, current_location):
        """
        Returns true if location 'v' contains a searcher AND
        is visible from the current vantage point.
        :param v: the location where a searcher could be
        :param current_location: the current vantage point
        :return: true if location 'v' contains a searcher AND
        is visible from the current vantage point, false otherwise.
        """
        raise NotImplementedError('Should be implemented by subclasses')

    @abc.abstractmethod
    def move_lost_person(self, start, end):
        """
        Moves a lost person from the start location to the end location,
        if allowed by the map.
        :param start: starting vertex (tuple)
        :param end: ending vertex (tuple)
        :return: true if move was successful, false otherwise
        """
        raise NotImplementedError('Should be implemented by subclasses')

    @abc.abstractmethod
    def move_searcher(self, start, end):
        """
        Moves a searcher from the start location to the end location,
        if allowed by the map.
        :param start: starting vertex (tuple)
        :param end: ending vertex (tuple)
        :return: true if move was successful, false otherwise
        """
        raise NotImplementedError('Should be implemented by subclasses')

    @abc.abstractmethod
    def spawn_lost_person(self, start):
        """
        Spawns a new lost person at the provided starting location.
        :param start: the starting location for the lost person
        :return:
        """
        raise NotImplementedError('Should be implemented by subclasses')

    @abc.abstractmethod
    def spawn_searcher(self, start):
        """
        Spawns a new searcher at the provided starting location.
        :param start: the starting location for the searcher
        :return:
        """
        raise NotImplementedError('Should be implemented by subclasses')

    @abc.abstractmethod
    def recover_lost_person(self, v):
        """
        Recovers a lost person by removing him from the map.
        :param v: the lost person's location
        :return:
        """
        raise NotImplementedError('Should be implemented by subclasses')

    @abc.abstractmethod
    def print(self):
        """
        Prints a text version of the grid graph, including locations
        of the different units.
        :return: None
        """
        raise NotImplementedError('Should be implemented by subclasses')

    @abc.abstractmethod
    def numRows(self):
        """
        Returns number of rows
        :return: number of rows
        """
        raise NotImplementedError('Should be implemented by subclasses')

    @abc.abstractmethod
    def numColumns(self):
        """
        Returns number of columns
        :return: number of columns
        """
        raise NotImplementedError('Should be implemented by subclasses')

    @abc.abstractmethod
    def get_shortest_path(self, start, end):
        """
        The shortest path between two points in the map
        :param start: Starting point
        :param end: Ending point
        :return:
        """