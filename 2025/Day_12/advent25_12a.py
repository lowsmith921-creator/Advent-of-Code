import sys
import os
import re
import math
import re

def rot90 (pnts, xs, ys) :
    retVal = []
    for p in pnts :
        px = p[1]
        py = p[0]
        retVal.append((px,py))

    return(retVal)

def flipX (pnts, xs, ys) :
    retVal = []
    for p in pnts :
        px = (xs-1) - p[0]
        py = p[1]
        retVal.append((px,py))

    return(retVal)

def flipY (pnts, xs, ys) :
    retVal = []
    for p in pnts :
        px = p[0]
        py = (ys-1) - p[1]
        retVal.append((px,py))

    return(retVal)

 
def main():
    
    try:
        with open("advent25_12.txt", "r") as f:
            inpList = [z.strip() for z in f.readlines()]
    except FileNotFoundError:
        print("Input file not found.")
        return

    I = 0
    ans = 0
    patts = dict()
    while I < len(inpList):
        if re.fullmatch(r'^[0-9]:', inpList[I]) :
            pnbr = inpList[I][0]
            
            pat = []
            while(True) :
                I += 1
                if inpList[I].strip() == "" :
                    break
                pat.append(inpList[I])
            patts[pnbr] = pat
        else :
            if re.match(r'^([0-9])+x([0-9])+:', inpList[I]) :
                glist = inpList[I].split()
                sz = glist[0].replace(":","")
                x = int(sz.split("x")[0])
                y = int(sz.split("x")[1])
                plist = [int(a) for a in glist[1:]]

                nx = int(x / 3)
                ny = int(y / 3)

                if (nx * ny ) >= sum(plist) :
                    ans += 1
                    print("pass")

                
            I += 1

    print(ans)


    #pDict = dict()
    #for p in patts :
    #    pnts = []
    #    for x in range(len(patts[p][0])) :
    #        for y in range(len(patts[p])) :
    #            if patts[p][y][x] == '#' :
    #                pt = (x,y)
    #                pnts.append(pt)
    #    pDict[p] = pnts


    #for p in pDict :
    #    newp = rot90(pDict[p], 3, 3)

            

            

         
if __name__ == "__main__":
    main()


 
