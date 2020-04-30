
from argparse import ArgumentParser
from corpus import BratCorpus#, PTBCorpus

text = "SRL tools"

parser = ArgumentParser(description = text)

parser.add_argument('--fscore', metavar="dir", nargs=2,
help="Get the balanced f-score between two directories")

parser.add_argument('--convert', metavar="dir",
help="Convert a directory of files with PTB + SRL to UDv2 + SRL")

parser.add_argument('--print', metavar="name", help="Print a file or directory in .ann format")

args = parser.parse_args()

def to_set(corpus):
    '''
    This is a helper function for below, to compensate for the issues with the
    OO tree structure
    '''
    result = set()
    for file_component in corpus:
        name = file_component.get_name()
        for token in file_component:
            list_token = token.as_string().split()
            list_token.append(name)
            result.add(tuple(list_token))
    return result

if args.print:
    dir_ = args.print

    corpus = BratCorpus("Corpus")

    corpus.perform_read(dir_)

    # print function
    corpus.print()
if args.convert:
    pass
if args.fscore:

    gold_dir, predicted_dir = args.fscore

    gold_corpus = BratCorpus("Gold Corpus") # initialize the corpora
    predicted_corpus = BratCorpus("Predicted Corpus")

    predicted_corpus.perform_read(predicted_dir) # read them in
    gold_corpus.perform_read(gold_dir)

    predicted_set = to_set(predicted_corpus) # convert to set
    gold_set = to_set(gold_corpus)

    intersection = predicted_set & gold_set # initialize variables for formula
    a = len(intersection)
    b = len(predicted_set - intersection)
    c = len(gold_set - intersection)

    print(f"F1 score: {(2 * a) / ((2 * a) + b + c)}") # give score

total_count = 0