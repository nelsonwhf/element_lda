import sys
__author__ = 'nelson'

def stat_cluster_size(infile,outfile,thred):
    cluster_size={}
    file_object=open(outfile,'w')
    for line in open(infile):
        probs=line.split(" ")
        l=len(probs)
        for i in range(0,l):
            print(probs[i])
            prob=float(probs[i])
            if prob>thred:
                cluster_size[i]=cluster_size.get(i,0)+1
    clusters=cluster_size.keys()
    for cluster in clusters:
        file_object.write(str(cluster)+" "+str(cluster_size.get(cluster,0)))
        file_object.flush()
    file_object.flush()
    file_object.close()

if __name__=='__main__':
    args=sys.argv
    print(args)
    stat_cluster_size(args[1],args[2],float(args[3]))
