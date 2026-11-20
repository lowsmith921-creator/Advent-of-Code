import sys
import os
import re
import math
import re


def getMax (inStr) :

    done = False
    while not done :
        for c in range (9,0,-1) :
            C = str(c)
            if C in inStr:
                CI = inStr.index(C)
                if CI < len(inStr)-1:
                    return(C+str(max([int(x) for x in inStr[CI+1:]])))
                else :
                    continue
                
        done = True
        

        
def main():
    
    try:
        with open("advent25_3.txt", "r") as f:
            inpList = [z.strip() for z in f.readlines()]
    except FileNotFoundError:
        print("Input file not found.")
        return

    tot = 0
    for i in inpList :
        tot += int(getMax(str(i)))


    print(tot)
        
if __name__ == "__main__":
    main()


 
