from abc import ABC, abstractmethod

class Aggregate(ABC):
    '''
    Interface for containers in the iterator protocol
    https://docs.python.org/3/library/stdtypes.html#iterator-types
    '''

    @abstractmethod
    def __iter__(self):
        pass