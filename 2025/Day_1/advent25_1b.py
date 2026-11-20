import sys
import os
import re
import math
import re

def spin(dialSize, cur, d, dist) :

    retVal = None
    
    if d == "L" :
        retVal = cur - dist
    elif d == "R":
        retVal = cur + dist
    
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
        x = t[0]
        y = int(t[1:])
        Y = int(y % dialSize)
        L = int(y / dialSize)
        
        new = spin(dialSize, cur, x, Y)
        #print(cur, x, y, Y, new)

        if new == 0 :
            ans += 1
        elif x == "R" and cur + Y >= dialSize :
            ans += 1
        elif x == "L" and cur != 0 and cur - Y < 0:
            ans += 1

        ans += L
        
        cur = new



    print(ans)
    
if __name__ == "__main__":
    main()


