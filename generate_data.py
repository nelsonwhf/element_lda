import logging, gensim, codecs, sys
__author__ = 'nelson'

def generate_dictionaries(infile,outfile):
    dictionary=gensim.corpora.Dictionary(line.lower().split() for line in open(infile))
    dictionary.save(outfile)
    print("dictionary save done!:\n"+dictionary.token2id)
    return dictionary

def generate_corpus(infile,outfile1,outfile2):



if __name__=='__main__':
    args=sys.argv
    print(args)