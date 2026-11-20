import sys
import os
import re
import math
import re
import itertools


def main():

    try:
        with open("advent25_6.txt", "r") as f:
            inpList = [z.strip() for z in f.readlines()]
    except FileNotFoundError:
        print("Input file not found.")
        return
    
    opers = [x for x in inpList[-1].split() ]
    #print(opers)
    ans = 0
    for ind in range(len(inpList[0].split())) :
        if opers[ind] == '+' :
            tot = 0
        elif opers[ind] == '*' :
            tot = 1
            
        for I,i in enumerate([int(x.split()[ind]) for x in inpList[:-1]]) :
            #print(I, i, opers[ind])
            if opers[ind] == '+' :
                #print("plus")
                tot += i
            elif opers[ind] == '*' :
                #print("times")
                tot *= i

        ans += tot
        #print(ind, tot)

    print(ans)

        
    
    
if __name__ == "__main__":
    main()


