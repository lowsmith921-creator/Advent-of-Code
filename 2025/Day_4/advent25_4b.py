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

    for yInd, y in enumerate(inpList):
        for xInd, x in enumerate(y) :
            matrix[(xInd,yInd)] = 0
            if x == '@' :
                p.append((xInd,yInd))


    done = False
    itr = 1
    tot = 0
    while not done :
        matrix = dict()
        for y in range(len(inpList)) :
            for x in range(len(inpList[0])) :
                matrix[(x,y)] = 0
                
        for x,y in p :
            for c in [(0,-1), (1,-1), (1, 0), (1,1), (0, 1), (-1,1), (-1, 0), (-1,-1) ] :
                if x+c[0] >=0 and x+c[0] < len(inpList[0]) and y+c[1] >= 0 and y+c[1] < len(inpList) :
                    matrix[(x+c[0],y+c[1])] += 1

        cnt = 0
        new_p = p[:]
        for x,y in p :
            if matrix[(x,y)] < 4 :
                cnt += 1
                new_p.remove((x,y))

        p = new_p[:]
        tot += cnt
        if cnt == 0 :
            done = True

    print(tot)

        
if __name__ == "__main__":
    main()
