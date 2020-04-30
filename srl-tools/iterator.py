from abc import ABC, abstractmethod

class Iterator(ABC):
    '''
    Interface to ensure that any implementing class complies with the iterator
    protocol https://docs.python.org/3/library/stdtypes.html#iterator-types
    '''

    @abstractmethod
    def __iter__(self):
        pass

    @abstractmethod
    def __next__(self):
        pass