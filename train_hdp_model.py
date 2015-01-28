import logging, gensim, codecs, sys

__author__ = 'nelson'

def train_model(dict_file,tfidf_file,model_file,topic_file,n):
    dictionary = gensim.corpora.dictionary.Dictionary.load(dict_file)
    tfidf = gensim.corpora.MmCorpus(tfidf_file)
    hdp = gensim.models.HdpModel(corpus=tfidf,id2word=dictionary,chunksize=10000)
    hdp.save(model_file)
    f = codecs.open(topic_file,'a','utf-8')
    f.write("\n".join(hdp.print_topics(topics=-1,topn=20)))
    f.close()

if __name__=='__main__':
    args=sys.argv
    print(args)
    train_model(args[1],args[2],args[3],args[4],int(args[4]))
