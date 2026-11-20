import sys
import os
import re
import math
import re
import itertools


def main():

    try:
        with open("advent25_6.txt", "r") as f:
            inpList = [z.replace("\n", "") for z in f.readlines()]
    except FileNotFoundError:
        print("Input file not found.")
        return
    
    opers = [x for x in inpList[-1].split() ]
    #print(opers)
        
    ans = 0
    for ind in range(len(inpList[0].split())-1, -1, -1) :
        if opers[ind] == '+' :
            tot = 0
        elif opers[ind] == '*' :
            tot = 1

    opr = opers.pop(0)
    if opr == '+' :
        tot = 0
    elif opr == '*' :
        tot = 1

    ans = 0
    for x in range(len(inpList[0])) :
        nbr = ''.join([a[x] for a in inpList[:-1]  ]).strip()
        if nbr != ""  :
            if opr == "+" :
                tot += int(nbr)
            elif opr == "*" :
                tot *= int(nbr)
        else :
            ans += tot
            opr = opers.pop(0)
            if opr == '+' :
                tot = 0
            elif opr == '*' :
                tot = 1

    ans += tot


    print(ans)
            
    
if __name__ == "__main__":
    main()


