import sys
import os
import re
import math
import re
from collections import deque
from functools import lru_cache

def press_button(board, buttons, i) :
    for b in buttons :
        board[b] += i 

    return(board)

def solveit (board, pattern, buttons) :
    queue = deque([(board, [])])
    visited = {tuple(board)}

    inc = 2
    while queue :
        curr_board, curr_moves = queue.popleft()

        #print(curr_board)
        if curr_board == pattern :
            return(curr_moves)
        else :
            toast = False
            for X,x in enumerate(curr_board) :
                if x > pattern[X] :
                    toast = True
            if toast :
                inc = 1
                continue

        for i in range(len(buttons)) :
            next_board = list(curr_board)
            press_button(next_board, buttons[i], inc)
            next_board_tuple = tuple(next_board)
            if next_board_tuple not in visited :
                visited.add(next_board_tuple)
                queue.append((next_board, curr_moves + [i]))

    return(None)
    
def main():
    
    try:
        with open("advent25_10_tst.txt", "r") as f:
            inpList = [z.strip() for z in f.readlines()]
    except FileNotFoundError:
        print("Input file not found.")
        return

    tot = 0

    for i in inpList :
        pattern = [x for x in i.split()[0][1:-1]]
        for Z, z in enumerate(pattern) :
            if z == '#' :
                pattern[Z] = 1
            elif  z == '.' :
                pattern[Z] = 0
        joltages = [int(a) for a in i.split()[-1][1:-1].split(",")]
        b = [y.split(",") for y in [x[1:-1] for x in i.split()[1:-1]]]
        buttons = []
        for a in b :
             buttons.append([int(y) for y in a])

        #print(pattern)
        #print(buttons)
        #print(joltages)
        board = [0]*len(pattern)
        #print(board, pattern)
        ret = solveit(board, joltages, buttons)
        print(ret)
        tot += len(ret)
        

        
    print(tot)
        
         
if __name__ == "__main__":
    main()


 
