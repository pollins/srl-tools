# Ultimately, this was not used

from iterator import Iterator

class CorpusIterator(Iterator):
    '''
    Concrete iterator for Corpus
    '''

    def __init__(self, iterator):
        '''
        Constructor method
        '''
        self.stack = [iterator]

    def __iter__(self):
        '''
        Returns this iterator object
        '''
        return self

    def __next__(self):
        
        if not self.stack:
            raise StopIteration
        else:
            it = self.stack[-1]
            component = it.__next__()

            stack.append(component.__iter__())
            self.stack.pop()
'''
        if self.has_next():
            iterator = self.stack[-1]
            component = iterator.__next__()

            self.stack.append(component.create_iterator())

            return component
        else:
            raise StopIteration
'''