import sys
import os
import re
import math
import re


        
def main():
    ans = 0
    try:
        with open("advent25_2.txt", "r") as f:
            inpList = [map(int, z.split("-")) for z in f.readline().strip().split(",")]
    except FileNotFoundError:
        print("Input file not found.")
        return
    tot = 0
    for x,y in inpList :
        z = [str(a) for a in range(x, y+1)]
        nl = [re.fullmatch(r"(.+)\1+", a) for a in z ]
        for n in nl:
            if n != None :
                tot += int(n[0])
                #print(n[0])


    print(tot)
if __name__ == "__main__":
    main()


 
