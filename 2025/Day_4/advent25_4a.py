import sys
import os
import re
import math
import re

                                 
        
def main():
    matrix = dict()
    try:
        with open("advent25_4.txt", "r") as f:
            inpList = [z.strip() for z in f.readlines()]
    except FileNotFoundError:
        print("Input file not found.")
        return
    
    p = []
    matrix = dict()
    for yInd, y in enumerate(inpList):
        for xInd, x in enumerate(y) :
            matrix[(xInd,yInd)] = 0
            if x == '@' :
                p.append((xInd,yInd))


    for x,y in p :
        for c in [(0,-1), (1,-1), (1, 0), (1,1), (0, 1), (-1,1), (-1, 0), (-1,-1) ] :
            if x+c[0] >=0 and x+c[0] < len(inpList[0]) and y+c[1] >= 0 and y+c[1] < len(inpList) :
                matrix[(x+c[0],y+c[1])] += 1

    cnt = 0
    for x,y in p :
        if matrix[(x,y)] < 4 :
            #print(x, y, matrix[(x,y)])
            cnt += 1

    print(cnt)

        
if __name__ == "__main__":
    main()
