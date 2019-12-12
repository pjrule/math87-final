import abc


class Partitioner(abc.ABC):
    @abc.abstractmethod
    def partition(self, scenario_map):
        raise NotImplementedError('Implemented by subclasses')