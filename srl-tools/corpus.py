from abc import abstractmethod
from aggregate import Aggregate
from corpus_iterator import CorpusIterator

class CorpusComponent(Aggregate):
    '''
    This is the component.
    '''
    
    # Common functions
    def get_index(self):
        raise TypeError

    # Leaf functions
    def get_label(self):
        raise TypeError

    def get_roleset(self):
        raise TypeError

    def get_dependent(self):
        raise TypeError

    def add_dependent(self, dependent): # this may take an index as a list or something
        raise TypeError

    # Composite function
    def add(self, component):
        raise TypeError

    def remove(self, component):
        raise TypeError

    def get_child(self, index):
        raise TypeError

    def __iter__(self):
        raise TypeError
    

class Corpus(CorpusComponent):
    '''
    This is the composite.
    '''

    def __init__(self, name):
        self.corpus_components = []
        self.name = name

    def __iter__(self):
        self.position = 0
        length = len(self.corpus_components)
        it = CorpusIterator(length)
        return it

    def add(self, corpus_component):
        self.corpus_components.append(corpus_component)
    
    def remove(self, corpus_component):
        self.corpus_components.remove(corpus_component)

    def get_child(self, index):
        return self.corpus_components[index]

    def print(self):
        print(f"Text: {self.name}")
        print(f"----------------")

        for corpus_component in self.corpus_components:
            corpus_component.print()


class Token(CorpusComponent):
    '''
    This is the leaf.
    '''

    def __init__(self, offset, label, roleset_id, relation):
        self.offset = offset
        self.label = label
        self.roleset_id = roleset_id
        self.relation = relation
    
    def get_offset(self):
        return self.offset
    
    def get_label(self):
        return self.label

    def get_roleset_id(self):
        return self.roleset_id

    def get_relation(self):
        return self.relation

    def print(self):
        print(f"{self.offset}\t{self.label}\t{self.roleset_id}")
        if self.relation != '_':
            print(f"--- Relation ---")
            self.relation.print()
            print("--- ---")