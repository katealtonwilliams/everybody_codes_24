from itertools import combinations_with_replacement
from math import lcm
import heapq

STAMPS_P1 = [1, 3, 5, 10]
STAMPS_P2 = [1, 3, 5, 10, 15, 16, 20, 24, 25, 30]

def find_min_beetles(input_file: str, stamps: list[int]) -> int:
    with open(input_file) as notes:
        sparkballs = [int(line.strip()) for line in notes.readlines()]
    beetle_count = 0
    stamps.sort(reverse=True)
    for sparkball in sparkballs:
        for stamp in stamps:
            if (no_beetles := sparkball // stamp) > 0:
                beetle_count += no_beetles
                sparkball %= stamp
    return beetle_count

def find_min_beetles_properly(input_file: str, stamps: list[int]) -> int:
    with open(input_file) as notes:
        sparkballs = [int(line.strip()) for line in notes.readlines()]
    beetle_count = 0
    stamps.sort(reverse=True)
    for sparkball in sparkballs:
        found_smallest_path = False
        if sparkball % stamps[0] == 0:
            beetle_count += sparkball / stamps[0]
            continue
        if sparkball // stamps[0] > 0:
            beetle_count += sparkball // stamps[0] - 1
            sparkball = sparkball % stamps[0] + stamps[0]
        paths = [(0, sparkball)]
        while found_smallest_path == False:
            length, remaining_sparkball = paths.pop()
            for stamp in stamps:
                updated_remaining_sparkball = remaining_sparkball - stamp
                if updated_remaining_sparkball == 0:
                    beetle_count += length + 1
                    found_smallest_path = True
                    break
                if updated_remaining_sparkball > 0:
                    paths.append((length+1, updated_remaining_sparkball))
            paths.sort(reverse=True)
    return beetle_count

if __name__ == "__main__":
    
    # part 1
    
    # print(find_min_beetles("day9/day9_inputs/day9_practise_p1.txt", STAMPS_P1))
    # print(find_min_beetles("day9/day9_inputs/day9_final_p1.txt", STAMPS_P1))
    
    # part 2
    
    print(find_min_beetles_properly("day9/day9_inputs/day9_practise_p2.txt", STAMPS_P2))
    print(find_min_beetles_properly("day9/day9_inputs/day9_final_p2.txt", STAMPS_P2))
    