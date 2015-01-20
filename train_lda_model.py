import logging, gensim, codecs, sys
__author__ = 'nelson'

def train_model(dict_file,tfidf_file,model_file,n):
    dictionary = gensim.corpora.dictionary.Dictionary.load(dict_file)
    tfidf = gensim.corpora.MmCorpus(tfidf_file)
    lda = gensim.models.ldamodel.LdaModel(corpus=tfidf, id2word=dictionary, num_topics=n, alpha='auto', eval_every=0, passes=20)
    lda.save(model_file)
    f = codecs.open('topics','a','utf-8')
    f.write("\n".join(lda.print_topics(n)))
    f.close()

if __name__=='__main__':
    args=sys.argv
    print(args)
    train_model(args[1],args[2],args[3])
