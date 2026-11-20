import sys
import os
import re
import math
import re

def spin(dialSize, cur, inst) :
    d = inst[0]
    dist = int(inst[1:])
    retVal = None
    
    if inst[0] == "L" :
        retVal = cur - dist
    elif inst[0] == "R":
        retVal = cur + dist

    retVal = retVal % dialSize
    
    if retVal < 0 :
        retVal = dialSize + retVal
    elif retVal >= dialSize :
        retVal = retVal - dialSize

    return(retVal)    
        
        
def main():
    ans = 0
    try:
        with open("advent25_1.txt", "r") as f:
            inpList = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("Input file not found.")
        return

    cur = 50
    dialSize = 100
    for t in inpList:
        new = spin(dialSize, cur, t)
        cur = new
        if cur == 0 :
            ans += 1


    print(ans)
    
if __name__ == "__main__":
    main()


