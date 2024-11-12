import numpy as np
from copy import deepcopy


def read_input_p1(file_name: str) -> np.ndarray:
    with open(file_name) as raw_image:
        grid = np.array(
            [
                [*line.strip().replace(".", "0").replace("#", "1")]
                for line in raw_image.readlines()
            ]
        )
    return grid.astype(int)


def get_neighbours(grid: np.ndarray, row: int, column: int) -> list[str]:
    surrounding_coords = [
        (row - 1, column),
        (row, column - 1),
        (row, column + 1),
        (row + 1, column),
    ]
    return [grid[coord] for coord in surrounding_coords]


def calculate_layer(grid: np.ndarray, layer_number: int) -> np.ndarray:
    new_layer = False
    updated_grid = deepcopy(grid)
    rows, columns = np.where(grid == layer_number)
    for row, column in zip(rows, columns):
        if all(
            layer_number == int(neighbour)
            for neighbour in get_neighbours(grid, row, column)
        ):
            updated_grid[row, column] = layer_number + 1
            new_layer = True
    return updated_grid, new_layer


def calculate_all_layers(file_name: str) -> int:
    current_grid = read_input_p1(file_name)
    more_layers = True
    layer_number = 1
    while more_layers == True:
        current_grid, more_layers = calculate_layer(current_grid, layer_number)
        layer_number += 1
    return np.sum(current_grid)


if __name__ == "__main__":
    # part 1

    print(calculate_all_layers("day3/day3_inputs/day3_practise_p1.txt"))
    print(calculate_all_layers("day3/day3_inputs/day3_final_p1.txt"))
