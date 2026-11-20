import sys
import os
import re
import math
import re

visited = set()

def shoot_beam(pos, inpList) :
    #print("enter", pos)
    global visited
    cur = list(pos)
    while(True) :
        cur[1] += 1
        #print(cur)
       
        if cur[1] >= len(inpList) :
            #print("exit")
            return
        if inpList[cur[1]][cur[0]] == '.' :
            continue
        elif inpList[cur[1]][cur[0]] == '^' :
            #split
            if (cur[0],cur[1]) not in visited :
                visited.add((cur[0],cur[1]))
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

    #for i in inpList :
    #    print(i)

    shoot_beam ((start,0), inpList)

    print(len(visited))

    
        
if __name__ == "__main__":
    main()


 
