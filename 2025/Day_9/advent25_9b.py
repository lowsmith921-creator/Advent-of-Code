import sys
import os
import re
import math
import re

        
def main():
    
    try:
        with open("advent25_9_tst.txt", "r") as f:
            inpList = [z.strip() for z in f.readlines()]
    except FileNotFoundError:
        print("Input file not found.")
        return

    coords = []
    for x,y in [a.split(",") for a in inpList] :
        coords.append((int(x), int(y)))

    for xs in set(s[0] for s in coords) :
        pts = [(a,b) for (a,b) in coords if a == xs]

        print(pts)

    for ys in set(s[1] for s in coords) :
        pts = [(a,b) for (a,b) in coords if b == ys]

        print(pts)
     
        
if __name__ == "__main__":
    main()


 
