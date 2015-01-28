import sys
__author__ = 'nelson'

def filter_users(infile,outfile):
    file_object=open(outfile,'w')
    for line in open(infile):
        parts=line.split(" ")
        id=parts[0]
        pros=parts[1:-1]
        maxpro=max(pros)
        index=pros.index(maxpro)
        file_object.write(str(id)+","+str(index)+'\n')
        file_object.flush()
    file_object.flush()
    file_object.close()

if __name__=='__main__':
    args=sys.argv
    print(args)
    filter_users(args[1],args[2])
