import sys
import time
import datetime

__author__ = 'nelson'

def calOrderTime(infile,outfile):
    writer = open(outfile,'w')
    for line in open(infile):
        parts = line.split(',')
        if(len(parts)<=2):
            continue
        uid = parts[0]
        length = len(parts)
        total = 0.0
        for i in xrange(1,length-1):
            print(parts[i]+' '+parts[i+1])
            d1 = datetime.datetime.strptime(parts[i],'%Y%m%d')
            d2 = datetime.datetime.strptime(parts[i+1],'%Y%m%d')
            total += (d2-d1).days
        avg = total/(length-2)
        writer.write(str(uid)+' '+str(avg)+'\n')
        writer.flush()
    writer.flush()
    writer.close()

if __name__ == '__main__':
    args = sys.argv
    print(args)
    calOrderTime(args[1],args[2])
