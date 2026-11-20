import sys
import os
import re
import math
import re
from collections import deque


def press_button(board, buttons) :
    for b in buttons :
        board[b] = 1 - board[b]

    return(board)

def solveit (board, pattern, buttons) :
    queue = deque([(board, [])])
    visited = {tuple(board)}

    while queue :
        curr_board, curr_moves = queue.popleft()

        if curr_board == pattern :
            return(curr_moves)

        for i in range(len(buttons)) :
            next_board = list(curr_board)
            press_button(next_board, buttons[i])
            next_board_tuple = tuple(next_board)

            if next_board_tuple not in visited :
                visited.add(next_board_tuple)
                queue.append((next_board, curr_moves + [i]))

    return(None)
    
def main():
    
    try:
        with open("advent25_10.txt", "r") as f:
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
        joltage = [int(a) for a in i.split()[-1][1:-1].split(",")]
        b = [y.split(",") for y in [x[1:-1] for x in i.split()[1:-1]]]
        buttons = []
        for a in b :
             buttons.append([int(y) for y in a])

        #print(pattern)
        #print(buttons)
        #print(joltage)
        board = [0]*len(pattern)
        #print(board, pattern)
        ret = solveit(board, pattern, buttons)
        #print(ret)
        tot += len(ret)
        

        
    print(tot)
        
         
if __name__ == "__main__":
    main()


 
