import sys
import os
import re
import math
import re

visited = set()
exits = 0

def shoot_beam(pos, inpList) :
    #print("enter", pos)
    global exits
    cur = list(pos)
    while(True) :
        cur[1] += 1
        #print(cur)
       
        if cur[1] >= len(inpList)-1 :
            #print("exit")
            exits += 1
            return
        if inpList[cur[1]][cur[0]] == '.' :
            continue
        elif inpList[cur[1]][cur[0]] == '^' :
            #split
            #print("SPLIT")
            shoot_beam ((cur[0]+1, cur[1]), inpList)
            shoot_beam ((cur[0]-1, cur[1]), inpList)
            return
        
def main():
    
    try:
        with open("advent25_7.txt", "r") as f:
            inpList = [z.strip() for z in f.readlines()]
    except FileNotFoundError:
        print("Input file not found.")
        return

    start = inpList[0].index("S")

    for i in inpList :
        print(i)

    shoot_beam ((start,0), inpList)

    print(exits)

    
        
if __name__ == "__main__":
    main()


 
