from statistics import median


def find_total_strikes_p1(file_name: str) -> int:
    with open(file_name) as raw_nails:
        nail_heights = [int(nail.strip()) for nail in raw_nails.readlines()]
    strike_count = 0
    shortest_nail = min(nail_heights)
    for nail in nail_heights:
        strike_count += nail - shortest_nail
    return strike_count


def find_total_strikes_p3(file_name: str) -> int:
    with open(file_name) as raw_nails:
        nail_heights = [int(nail.strip()) for nail in raw_nails.readlines()]
    strike_count = 0
    median_nail = median(nail_heights)
    for nail in nail_heights:
        strike_count += abs(nail - median_nail)
    return strike_count


if __name__ == "__main__":
    # part 1

    print(find_total_strikes_p1("day4/day4_inputs/day4_practise_p1.txt"))
    print(find_total_strikes_p1("day4/day4_inputs/day4_final_p1.txt"))

    # part 2

    print(find_total_strikes_p1("day4/day4_inputs/day4_final_p2.txt"))

    # part 3

    print(find_total_strikes_p3("day4/day4_inputs/day4_practise_p3.txt"))
    print(find_total_strikes_p3("day4/day4_inputs/day4_final_p3.txt"))
