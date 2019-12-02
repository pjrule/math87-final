import abc


class LostPerson(abc.ABC):
    """
    A Lost Person is exactly what you would imagine - someone who is lost.
    In our simulation, a lost person moves once per time step. At each time
    step, he may move one or more units in any direction,
    starting from his current location. Where exactly he moves is defined
    by the subclass implementing this interface.
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
    def get_history(self):
        """
        Gets a list of locations at which this person was located, ordered
        by time visited.
        :return: ordered list of visited locations
        """
        raise NotImplementedError('Should be implemented by subclasses')
