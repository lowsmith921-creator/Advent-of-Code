import sys
import os
import re
import math
import re


def getMax (inStr) :

    max_skip = len(inStr) - 12
    
    new_nbr = []
    for c in inStr :
        #skip if new_nbr is empty, if we are out of skips or
        #if the last digit of the new number is smaller than the one we are checking
        while new_nbr and max_skip > 0 and new_nbr[-1] < c :
            #replace the last number with the current one
            new_nbr.pop()
            max_skip -= 1
        new_nbr.append(c)

    retVal = ''.join(new_nbr[:12])
    
    print(retVal)
    return(int(retVal))
               

        
def main():
    
    try:
        with open("advent25_3_tst.txt", "r") as f:
            inpList = [z.strip() for z in f.readlines()]
    except FileNotFoundError:
        print("Input file not found.")
        return

    tot = 0
    for i in inpList :
        tot += getMax([x for x in str(i)])


    print(tot)
        
if __name__ == "__main__":
    main()


 
