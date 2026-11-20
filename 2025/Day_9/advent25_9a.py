import sys
import os
import re
import math
import re
        

    


        
def main():
    
    try:
        with open("advent25_9.txt", "r") as f:
            inpList = [z.strip() for z in f.readlines()]
    except FileNotFoundError:
        print("Input file not found.")
        return

    coords = []
    for x,y in [a.split(",") for a in inpList] :
        coords.append((int(x), int(y)))

    max_area = 0
    for A,a in enumerate(coords) :
        for B, b in enumerate(coords) :
            l = abs(b[0]-a[0])+1
            w = abs(b[1]-a[1])+1
            area = l * w
            #print(max_area, area, l, w, a, b)
            if area > max_area :
                max_area = area


    print(max_area)
        
        
if __name__ == "__main__":
    main()


 
