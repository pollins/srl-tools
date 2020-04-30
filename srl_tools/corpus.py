from abc import abstractmethod
from aggregate import Aggregate
from corpus_iterator import CorpusIterator
from os import scandir

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

    def get_relation(self):
        raise TypeError

    def set_relation(self, relation):
        return TypeError

    # Composite function
    def add(self, component):
        raise TypeError

    def remove(self, component):
        raise TypeError

    def get_child(self, index):
        raise TypeError

    def perform_read(self, dirname):
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
        it = self.corpus_components.__iter__()
        return it

    def add(self, corpus_component):
        self.corpus_components.append(corpus_component)
    
    def remove(self, corpus_component):
        self.corpus_components.remove(corpus_component)

    def get_child(self, index):
        return self.corpus_components[index]

    def get_name(self):
        return self.name

    def perform_read(self, dirname):
        '''
        Perform method for strategy pattern.
        '''
        self.read(dirname)

    def print(self):
        '''
        The print method can recur, as in Head First.
        '''
        print(f"Text: {self.name}")
        print(f"----------------")

        for corpus_component in self.corpus_components:
            corpus_component.print()

class BratCorpus(Corpus):
    '''
    This is the first type of corpus for the strategy pattern
    '''
    def read(self, dirname):
        '''
        This reads in .ann files
        '''
        dir = scandir(dirname)
        for entry in dir:
            filename = entry.name
            entries = {}
            roleset_ids = {}
            relations = {}
            file_corpus = BratCorpus(filename) # initialize the sub-corpus to our specific format
            file = open(entry.path, encoding='utf-8')
            
            for line in file:
                line = line.split()
                key = line[0]
                if key.startswith('T'): # this indicates a label
                    entries[key] = Token(line[2], line[1])
                elif key.startswith('#'): # this indicates the roleset, i.e., the identity of a verb
                    t_index = line[2] # it is only present on verbs
                    roleset_id = line[3]
                    roleset_ids[t_index] = roleset_id
                elif key.startswith('R'): # this indicates the relation (arrow) from a predicate to a verb
                    source_t_index = line[2].split(':')[-1] 
                    target_t_index = line[3].split(':')[-1]
                    relations[source_t_index] = target_t_index
            
            for key in roleset_ids: # populate dictionary of rolesets
                entries[key].set_roleset_id(roleset_ids[key])
            for key in relations: # populate dictionary of relations
                # relation = entries[relations[key]] note this line is for if we
                # want to change to relations, for now we just want relation id
                relation = relations[key]
                entries[key].set_relation(relation)

            for entry in entries.values(): # finally, populate the sub-corpus with the entries
                file_corpus.add(entry)
            self.add(file_corpus) # then add that subcorpus to the main corpus



class Token(CorpusComponent):
    '''
    This is the leaf.
    '''

    def __init__(self, offset, label):
        self.offset = offset
        self.label = label
        self.roleset_id = '_'
        self.relation = '_'

    def __iter__(self):
        return None

    def set_roleset_id(self, roleset_id):
        self.roleset_id = roleset_id

    def set_relation(self, relation):
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
        print(self.as_string())
        if self.relation != '_':
            print(f"--- Relation ---")
            # print(self.relation._as_string()) again, if relations need to be tokens
            print(self.relation)
            print("--- ---")
    
    def as_string(self):
        return (self.offset + '\t' + self.label + '\t' + self.roleset_id)