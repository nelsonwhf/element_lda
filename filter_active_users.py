import sys
__author__ = 'nelson'

def filter_users(infile,outfile,thred):
    file_object=open(outfile,'w')
    for line in open(infile):
        probs=line.split(" ")
        l=len(probs)
        if l-1>thred:
            file_object.write(line+"\n")
            file_object.flush()
    file_object.flush()
    file_object.close()

if __name__=='__main__':
    args=sys.argv
    print(args)
    filter_users(args[1],args[2],int(args[3]))