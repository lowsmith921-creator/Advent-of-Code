import sys
import os
import re
import math
import re
        
def get_nearest(inpList) :

    pts = []
    retPts = []
    for i in [x for x in inpList] :
        pts.append(([int(x) for x in i.split(",")]))

    
    for P,p in enumerate(pts[:-1]) :
        for A,a in enumerate(pts[P+1:]) :
            x = (math.sqrt((p[0] - a[0])**2 + \
                     (p[1] - a[1])**2 + \
                     (p[2] - a[2])**2 ))

            retPts.append((p, a, x))
 
    return(sorted(retPts, key=lambda x: x[2]))
    

def check_circs (circs, pt ):

    for C, c in enumerate(circs) :
        if pt in c :
            return(C)

    return(None)
    
        
def main():
    
    try:
        with open("advent25_8_tst.txt", "r") as f:
            inpList = [z.strip() for z in f.readlines()]
    except FileNotFoundError:
        print("Input file not found.")
        return


    pr = get_nearest(inpList)
    circs = []
    for I, i in enumerate(pr):
        chkA = check_circs(circs, i[0])
        chkB = check_circs(circs, i[1])

        print(i, chkA, chkB)
        if chkA != None and chkB == None:
            print("add b to a")
            circs[chkA].append(i[1])
        elif chkA == None and chkB != None:
            print("add a to b")
            circs[chkB].append(i[0])
        elif chkA == None and chkB == None :
            print("new circuit")
            circs.append([i[0], i[1]])
        elif chkA != None and chkB != None :
            if chkA == chkB :
                print("skip")
                pass
            else :
                print("combine", chkA, chkB)
                for x in circs[chkA] :
                    circs[chkB].append(x)
                circs.pop(chkA)


        if I > 10 and len(circs) == 1 :
            print(i)
            break
        
            
                
        

    ans = 1
    for i in sorted([len(x) for x in circs])[::-1][:3] :
        #print(i)
        ans *= i
         
    print(ans)
        
        
if __name__ == "__main__":
    main()


 
