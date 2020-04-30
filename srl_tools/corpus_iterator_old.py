from iterator import Iterator

class CorpusIterator(Iterator):
    '''
    Concrete iterator for Corpus
    '''

    def __init__(self, components):
        '''
        Constructor method
        '''
        self.components = components
        self.num = 0

    def __iter__(self):
        '''
        Returns this iterator object
        '''
        return self

    def __next__(self):
        '''
        Uses the "generator pattern" https://wiki.python.org/moin/Generators
        '''
        if self.num < len(self.components):
            cur, self.num = self.num, self.num + 1
            return self.components[cur]
        else:
            raise StopIteration