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
    def get_next(self, scenario_map, current):
        """
        Computes the next location where the lost person will move.
        :param scenario_map: the scenario map
        :param current: the lost person's current location.
        :return: the new current location for the lost person after moving.
        """
        raise NotImplementedError('Should be implemented by subclasses')
