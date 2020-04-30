from iterator import Iterator

class CorpusIterator(Iterator):
    '''
    Concrete iterator for Corpus
    '''

    def __init__(self, length):
        '''
        Constructor method
        '''
        self.length = length
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
        if self.num < self.length:
            cur, self.num = self.num, self.num + 1
            return cur
        else:
            raise StopIteration