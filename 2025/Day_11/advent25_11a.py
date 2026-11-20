import sys
import os
import re
import math
import re
from collections import deque

def getPaths (mach, start, path=[]) :

    path += [start]

    if start == 'out':
        #if 'fft' in path and 'dac' in path :
        return([path])
        #else :
        #    return([])

    if start not in mach :
        return([])

    paths = []
    for n in mach[start] :
        if n not in path :
            newPaths = getPaths(mach, n, path.copy())
            #print(newPaths)
            for new in newPaths :
                paths.append(new)
                
    return(paths)
    

    
    
def main():
    
    try:
        with open("advent25_11.txt", "r") as f:
            inpList = [z.strip() for z in f.readlines()]
    except FileNotFoundError:
        print("Input file not found.")
        return

    tot = 0

    mach = dict()
    
    for i in inpList :
        outs = [j for j in i.split()[1:]]
        mkey = i.split()[0].replace(':', '')
        mach[mkey] = outs


    ret = getPaths(mach, 'svr')
    cnt = 0
    for x in ret :
        if 'fft' not in x or 'dac' not in x :
            continue
        cnt += 1

    print(cnt)
    
         
if __name__ == "__main__":
    main()


 
