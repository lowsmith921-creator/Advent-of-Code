import sys
import os
import re
import math
import re
import itertools
from typing import List, Tuple

def merge_intervals(intervals: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    if not intervals:
        return []
    # Sort by start
    intervals_sorted = sorted(intervals, key=lambda x: x[0])
    merged = []
    current_start, current_end = intervals_sorted[0]
    for s, e in intervals_sorted[1:]:
        if s <= current_end + 1:
            if e > current_end:
                current_end = e
        else:
            merged.append((current_start, current_end))
            current_start, current_end = s, e
    merged.append((current_start, current_end))
    return merged
                                 
def count_total_numbers(intervals: List[Tuple[int, int]]) -> int:
    return sum(e - s + 1 for s, e in intervals)

def main():

    try:
        with open("advent25_5.txt", "r") as f:
            inpList = [z.strip() for z in f.readlines()]
    except FileNotFoundError:
        print("Input file not found.")
        return
    

    bl = inpList.index("")
   
    fresh = [list(map(int, a.split("-"))) for a in inpList[:bl]]

    ing = [int(c) for c in inpList[bl+1:]]


    merged = merge_intervals(fresh)
    total = count_total_numbers(merged)
    print(total)
    
    
if __name__ == "__main__":
    main()


