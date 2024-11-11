potion_map = {"A": 0, "B": 1, "C": 3, "D": 5, "x": 0}


def calculate_potions_p1(input_file: str) -> int:
    with open(input_file) as creatures:
        creatures = creatures.readline().strip()
    total_potions = 0
    for enemy, potions in potion_map.items():
        total_potions += creatures.count(enemy) * potions
    return total_potions


def calculate_potions_p2(input_file: str, groupsize=2) -> int:
    with open(input_file) as creatures:
        creatures = creatures.readline().strip()
    pairwise_enemies = [
        creatures[i] + creatures[i + 1] for i in range(0, len(creatures), 2)
    ]
    total_potions = 0
    for pair in pairwise_enemies:
        for enemy, potions in potion_map.items():
            total_potions += pair.count(enemy) * potions
        if "x" not in pair:
            total_potions += 2
    return total_potions


def calculate_potions_p3(input_file: str) -> int:
    with open(input_file) as creatures:
        creatures = creatures.readline().strip()
    pairwise_enemies = [
        creatures[i] + creatures[i + 1] + creatures[i + 2]
        for i in range(0, len(creatures), 3)
    ]
    total_potions = 0
    for pair in pairwise_enemies:
        for enemy, potions in potion_map.items():
            total_potions += pair.count(enemy) * potions
        if "x" not in pair:
            total_potions += 6
        if pair.count("x") == 1:
            total_potions += 2
    return total_potions


if __name__ == "__main__":
    # part 1

    print(calculate_potions_p1("day1/day1_inputs/day1_practise_p1.txt"))
    print(calculate_potions_p1("day1/day1_inputs/day1_final_p1.txt"))

    # part 2

    print(calculate_potions_p2("day1/day1_inputs/day1_practise_p2.txt"))
    print(calculate_potions_p2("day1/day1_inputs/day1_final_p2.txt"))

    # part 3
    print(calculate_potions_p3("day1/day1_inputs/day1_practise_p3.txt"))
    print(calculate_potions_p3("day1/day1_inputs/day1_final_p3.txt"))
