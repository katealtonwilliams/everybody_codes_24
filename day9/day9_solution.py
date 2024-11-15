from itertools import combinations_with_replacement
from copy import deepcopy

STAMPS_P1 = [1, 3, 5, 10]
STAMPS_P2 = [1, 3, 5, 10, 15, 16, 20, 24, 25, 30]

def find_min_beetles(input_file: str, stamps: list[int]) -> int:
    with open(input_file) as notes:
        sparkballs = [int(line.strip()) for line in notes.readlines()]
    beetle_count = 0
    stamps.sort(reverse=True)
    for sparkball in sparkballs:
        max_beetles = 0
        decreasing_sparkball = deepcopy(sparkball)
        for stamp in stamps:
            if (no_beetles := sparkball // stamp) > 0:
                max_beetles += no_beetles
                decreasing_sparkball %= stamp
        estimated_min = sparkball // stamps[0]
        found_smaller = False
        for comb_size in range(estimated_min, max_beetles):
            for potential_combination in combinations_with_replacement(stamps, comb_size):
                if sum(potential_combination) == sparkball:
                    found_smaller = True
                    break
            break
        if found_smaller:
            beetle_count += comb_size
        else:
            beetle_count += max_beetles
    return beetle_count

if __name__ == "__main__":
    
    # part 1
    
    print(find_min_beetles("day9/day9_inputs/day9_practise_p1.txt", STAMPS_P1))
    print(find_min_beetles("day9/day9_inputs/day9_final_p1.txt", STAMPS_P1))
    
    # part 2
    
    print(find_min_beetles("day9/day9_inputs/day9_practise_p2.txt", STAMPS_P2))
    # print(find_min_beetles("day9/day9_inputs/day9_final_p1.txt", STAMPS_P1))
    