import numpy as np
from copy import deepcopy
from typing import Callable


def read_input(file_name: str) -> np.ndarray:
    with open(file_name) as raw_image:
        grid = np.array(
            [
                [*line.strip().replace(".", "0").replace("#", "1")]
                for line in raw_image.readlines()
            ]
        )
    return np.pad(grid.astype(int), pad_width=2, mode="constant", constant_values=0)


def get_neighbours_p1(grid: np.ndarray, row: int, column: int) -> list[str]:
    surrounding_coords = [
        (row - 1, column),
        (row, column - 1),
        (row, column + 1),
        (row + 1, column),
    ]
    return [grid[coord] for coord in surrounding_coords]


def get_neighbours_p3(grid: np.ndarray, row: int, column: int) -> list[str]:
    max_row, max_column = grid.shape
    surrounding_coords = [
        (row - 1, column - 1),
        (row - 1, column),
        (row - 1, column + 1),
        (row, column - 1),
        (row, column + 1),
        (row + 1, column - 1),
        (row + 1, column),
        (row + 1, column + 1),
    ]
    return [
        grid[(row, column)]
        for row, column in surrounding_coords
        if row < max_row and column < max_column and row > 0 and column > 0
    ]


def calculate_layer(
    grid: np.ndarray, layer_number: int, neighbour_func: Callable
) -> np.ndarray:
    new_layer = False
    updated_grid = deepcopy(grid)
    rows, columns = np.where(grid == layer_number)
    for row, column in zip(rows, columns):
        if all(
            layer_number == neighbour for neighbour in neighbour_func(grid, row, column)
        ):
            updated_grid[row, column] = layer_number + 1
            new_layer = True
    return updated_grid, new_layer


def calculate_all_layers(file_name: str, neighbour_func: Callable) -> int:
    current_grid = read_input(file_name)
    more_layers = True
    layer_number = 1
    while more_layers == True:
        current_grid, more_layers = calculate_layer(
            current_grid, layer_number, neighbour_func
        )
        layer_number += 1
    return np.sum(current_grid)


if __name__ == "__main__":
    # part 1

    print(
        calculate_all_layers("day3/day3_inputs/day3_practise_p1.txt", get_neighbours_p1)
    )
    print(calculate_all_layers("day3/day3_inputs/day3_final_p1.txt", get_neighbours_p1))

    # part 2

    print(calculate_all_layers("day3/day3_inputs/day3_final_p2.txt", get_neighbours_p1))

    # part 3

    print(
        calculate_all_layers("day3/day3_inputs/day3_practise_p1.txt", get_neighbours_p3)
    )
    print(calculate_all_layers("day3/day3_inputs/day3_final_p3.txt", get_neighbours_p3))
