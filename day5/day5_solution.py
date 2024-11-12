import numpy as np
from copy import deepcopy


def create_grid_p1(input_file: str) -> np.ndarray:
    with open(input_file) as raw_input:
        initial_grid = []
        for line in raw_input.readlines():
            new_line = [int(number) for number in line.split()]
            initial_grid.append(new_line)
    initial_grid = np.array(initial_grid)
    return np.pad(initial_grid, pad_width=1, mode="constant", constant_values=0)


def get_new_position(clap_number: int, col: np.ndarray) -> int:
    col_length = len(np.delete(col, np.where(col == 0)))
    if clap_number <= col_length:
        return clap_number
    times_into = clap_number // col_length
    mod = clap_number % col_length
    if times_into % 2 == 0:
        return 2 if mod == 0 else mod
    return col_length if mod == 0 else col_length - (mod - 2)


def run_one_round(grid: np.ndarray, round_number: int) -> np.ndarray:
    base_column = 4 if (mod := round_number % 4) == 0 else mod
    change_column = base_column + 1 if base_column < 4 else 1
    clap_number = grid[1, base_column]
    clap_pos = get_new_position(clap_number, grid[:, change_column])
    updated_grid = deepcopy(grid)
    updated_grid[:, base_column] = np.concatenate(
        (np.array([0]), np.roll(grid[:, base_column], -1)[1:])
    )
    updated_grid[:, change_column] = np.concatenate(
        (
            grid[:clap_pos, change_column],
            np.array([clap_number]),
            grid[clap_pos:-1, change_column],
        )
    )
    return updated_grid


def run_n_rounds(input_file: str, no_rounds: int) -> int:
    current_grid = create_grid_p1(input_file)
    current_round = 1
    while current_round <= no_rounds:
        current_grid = run_one_round(current_grid, current_round)
        current_round += 1
    current_grid = np.char.mod("%i", current_grid)
    return int(int(("").join(current_grid[1])) / 10)


def find_length_of_dance(input_file: str, count_times: int) -> int:
    current_grid = create_grid_p1(input_file)
    current_round = 1
    number_dict = {}
    while all(values < count_times for values in number_dict.values()):
        current_grid = run_one_round(current_grid, current_round)
        first_row = np.char.mod("%i", current_grid[1])
        number = int(int(("").join(first_row)) / 10)
        if number not in number_dict:
            number_dict[number] = 1
        else:
            number_dict[number] += 1
        current_round += 1
    for key, value in number_dict.items():
        if value == count_times:
            return key * (current_round - 1)


if __name__ == "__main__":
    # # part 1

    # print(run_n_rounds("day5/day5_inputs/day5_practise_p1.txt", 10))
    # print(run_n_rounds("day5/day5_inputs/day5_final_p1.txt", 10))

    # part 2

    print(find_length_of_dance("day5/day5_inputs/day5_practise_p2.txt", 2024))
    print(find_length_of_dance("day5/day5_inputs/day5_final_p2.txt", 2024))
