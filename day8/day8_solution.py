import math


def read_in_number(input_file: str) -> int:
    with open(input_file) as notes:
        no_blocks = int(notes.readline().strip())
    return no_blocks


def calculate_answer_p1(blocks_given: int) -> int:
    n = math.ceil(blocks_given**0.5)
    bottom_row = 2 * n - 1
    return (n**2 - blocks_given) * bottom_row


def solution_p1(input_file: str) -> int:
    blocks = read_in_number(input_file)
    return calculate_answer_p1(blocks)


def find_cycle_of_thickness_p2(
    acolytes: int = 1111, high_priests: int = 722
) -> list[int]:
    cycle_of_thickness = []
    previous_thickness = 1
    for i in range(0, 100):
        cycle_of_thickness.append(previous_thickness)
        thickness = (previous_thickness * high_priests) % acolytes
        previous_thickness = thickness
        i += 1
    return cycle_of_thickness


def calculate_answer_p2(cycle_of_thickness: list[int], blocks_given: int = 20240000):
    previous_layer_number = 1
    blocks_needed = 1

    while blocks_needed < blocks_given:
        current_thickness = cycle_of_thickness[
            (previous_layer_number) % (len(cycle_of_thickness))
        ]
        base_length = 2 * (previous_layer_number + 1) - 1
        blocks_needed += current_thickness * base_length
        previous_layer_number += 1

    return (blocks_needed - blocks_given) * base_length


def find_cycle_of_thickness_p3(high_priests: int = 948722, acolytes: int = 10):
    cycle_of_thickness = []
    previous_thickness = acolytes + 1
    for i in range(0, 4):
        thickness = ((previous_thickness * high_priests) % acolytes) + acolytes
        cycle_of_thickness.append(thickness)
        previous_thickness = thickness
        i += 1
    return cycle_of_thickness


def calculate_answer_p3(
    cycle_of_thickness: list[int],
    layer_start: int = 0,
    blocks_given: int = 202_400_000,
    high_priests: int = 948722,
    acolytes: int = 10,
):
    shrine = [1]
    current_thickness = 1
    layer = layer_start
    blocks_needed = 0

    while blocks_needed < blocks_given:
        current_thickness = cycle_of_thickness[layer]
        shrine = [current_thickness + column for column in shrine]
        shrine = [current_thickness] + shrine
        shrine_width = len(shrine) * 2 - 1
        multiplier = shrine_width * high_priests
        numbers_to_remove = [
            2 * ((multiplier * height) % acolytes) for height in shrine[1:-1]
        ] + [((multiplier * shrine[-1]) % acolytes)]
        blocks_needed = sum(shrine) + sum(shrine[:-1]) - sum(numbers_to_remove)
        layer = (layer + 1) % len(cycle_of_thickness)
    return blocks_needed - blocks_given


if __name__ == "__main__":
    # part 1

    print(solution_p1("day8/day8_inputs/day8_practise_p1.txt"))
    print(solution_p1("day8/day8_inputs/day8_final_p1.txt"))

    # part 2

    print(calculate_answer_p2([1, 3, 4, 2], 50))
    print(calculate_answer_p2(find_cycle_of_thickness_p2()))

    # part 3

    print(calculate_answer_p3([6, 7, 9, 8], 1, 160, 2, 5))
    print(calculate_answer_p3(find_cycle_of_thickness_p3(), 0))
