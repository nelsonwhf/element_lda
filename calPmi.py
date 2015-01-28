import sys, itertools, math, numpy
__author__ = 'nelson'

def calPMI(topicFile,dataFile,outFile):
    (wordDic,pairDic)=calWordAndPairNum(dataFile)
    writer=open(outFile,'w')
    i=0
    for line in open(topicFile):
        pairs=getPairs(line)
        pmis=[]
        for pair in pairs:
            pxy=pairDic[pair]+0.0
            px=wordDic[pair[0]]
            py=wordDic[pair[1]]
            pmi=math.log(pxy/(px*py))
            pmis.append(pmi)
        avg=numpy.mean(pmis)
        media=numpy.median(pmis)
        writer.write(str(i)+' '+avg+' '+media+'\n')
        writer.flush()
        i=i+1
    writer.flush()
    writer.close()

def calWordAndPairNum(infile):
    wordDic={}
    pairDic={}
    i=0
    for line in open(infile):
        words=set(line.strip().split(' '))
        for w in words:
            wordDic[w]=wordDic.get(w,0)+1

        wordList=list(words)
        wordList.sort()
        pairs=list(itertools.combinations(wordList,2))
        for pair in pairs:
            pairDic[pair]=pairDic.get(pair,0)+1
        i=i+1
        if i%10000==0:
            print(str(i)+'th data cal done!')
    return (wordDic,pairDic)

def getPairs(line):
    words=list(set(line.strip().split('')))
    words.sort()
    pairs=list(itertools.combinations(words,2))
    return pairs

if __name__ == '__main__':
    args=sys.argv
    print(args)
    calPMI(args[1],args[2],args[3])
