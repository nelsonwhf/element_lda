import logging, gensim, codecs, sys
__author__ = 'nelson'

def generate_dictionaries(infile,outfile):
    dictionary=gensim.corpora.Dictionary(line.lower().split() for line in open(infile))
    dictionary.save(outfile)
    print("dictionary save done!:\n"+dictionary.token2id)
    return dictionary

def generate_corpus(raw_file,dict_file,bow_file,tfidf_file):
    dicionary=generate_dictionaries(raw_file,dict_file)
    corpus=[dicionary.doc2bow(line.lower().split()) for line in open(raw_file)]
    gensim.corpora.MmCorpus.serialize(bow_file, corpus)
    print("bow file save done!")

    tfidf = gensim.models.TfidfModel(corpus)
    corpus_tfidf = tfidf[corpus]
    gensim.corpora.MmCorpus.serialize(tfidf_file,corpus_tfidf)
    print("tfidf file save done!")



if __name__=='__main__':
    args=sys.argv
    print(args)
    generate_corpus(args[1],args[2],args[3])