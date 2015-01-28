import sys
__author__ = 'nelson'

def processTopics(infile,outfile):
    writer=open(outfile,'w')
    topics=[]
    for line in open(infile):
        if 'Topic' in line and len(topics)==0:
            continue
        elif 'Topic' in line and len(topics)!=0:
            writer.write(' '.join(topics)+'\n')
            writer.flush()
        else:
            parts=line.strip().split(' ')
            topics.append(parts[0])
    writer.flush()
    writer.close()

if __name__=='__main__':
    args=sys.argv
    print(args)
    processTopics(args[1],args[2])