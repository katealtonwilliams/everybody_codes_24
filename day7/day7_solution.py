import numpy as np
from typing import Callable
from itertools import permutations


def get_chariot_actions(input_file: str) -> dict[str]:
    chariot_action_map = {}
    with open(input_file) as notes:
        for note in notes.readlines():
            note = note.strip()
            chariot, actions = note.split(":")
            actions = actions.split(",")
            chariot_action_map[chariot] = actions
    return chariot_action_map


def parse_racecourse_p2(input_file: str) -> list[str]:
    right_side = ""
    left_side = ""
    with open(input_file) as notes:
        raw_track = notes.readlines()
    top = raw_track[0].strip()[1:]
    bottom = raw_track[-1].strip()[::-1]
    for track_segment in raw_track[1:-1]:
        track_segment = track_segment.split()
        right_side += track_segment[1].strip()
        left_side += track_segment[0].strip()
    return top + right_side + bottom + left_side + "="


def parse_racecourse_p3(input_file: str) -> np.ndarray:
    full_racecourse = []
    with open(input_file) as notes:
        for line in notes.readlines():
            full_racecourse.append([*line.strip()])
    for line in full_racecourse:
        if len(line) < 71:
            line.extend([" "] * (71 - len(line)))
    full_racecourse = np.array(full_racecourse)

    flattened_racecourse = ["+"]
    current_position = (0, 1)
    current_track = "+"
    came_from_direction = (0, -1)

    while current_track != "S":
        possible_directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        possible_directions.remove(came_from_direction)
        for direction in possible_directions:
            new_position = tuple(
                map(lambda pos, dir: pos + dir, current_position, direction)
            )
            if new_position[0] < 0 or new_position[0] > 9:
                continue
            if new_position[1] < 0 or new_position[1] > 70:
                continue
            if (new_track := full_racecourse[new_position]) != " ":
                current_position = new_position
                flattened_racecourse.append(str(new_track))
                current_track = new_track
                came_from_direction = tuple(-1 * i for i in direction)
                break
    return flattened_racecourse[:-1] + ["="]


def complete_race_p1(input_file: str, rounds: int) -> str:
    chariot_action_map = get_chariot_actions(input_file)
    final_scores = []
    for chariot, actions in chariot_action_map.items():
        current_round = 0
        current_power_level = 10
        total_power_level = 0
        while current_round < rounds:
            current_action = actions[current_round % len(actions)]
            if current_action == "+":
                current_power_level += 1
            if current_action == "-":
                if current_power_level > 0:
                    current_power_level -= 1
            total_power_level += current_power_level
            current_round += 1
        final_scores.append((total_power_level, chariot))
    final_scores.sort(reverse=True)
    final_standings = ""
    for chariot, power_level in final_scores:
        final_standings += power_level
    return final_standings


def complete_race_p2(
    chariot_input_file: str,
    racecourse_input_file: str,
    loops: int,
    parse_racecourse: Callable,
) -> str:
    if chariot_input_file.endswith("txt"):
        chariot_action_map = get_chariot_actions(chariot_input_file)
    else:
        chariot_action_map = {"A": [*chariot_input_file]}
    racecourse = parse_racecourse(racecourse_input_file)
    final_scores = []
    for chariot, actions in chariot_action_map.items():
        current_loop = 0
        current_power_level = 10
        total_power_level = 0
        current_round = 0
        while current_loop < loops:
            current_action = actions[current_round % len(actions)]
            current_track = racecourse[current_round % len(racecourse)]
            if current_track == "+" or current_track == "=" and current_action == "+":
                current_power_level += 1
            if current_track == "-" or current_track == "=" and current_action == "-":
                if current_power_level > 0:
                    current_power_level -= 1
            total_power_level += current_power_level
            if (current_round + 1) % len(racecourse) == 0:
                current_loop += 1
            current_round += 1
        final_scores.append((total_power_level, chariot))
    final_scores.sort(reverse=True)
    final_standings = ""
    for chariot, power_level in final_scores:
        final_standings += power_level
    return final_standings, final_scores


def find_winning_combos(
    chariot_input_file: str,
    racecourse_input_file: str,
    loops: int = 2024,
    parse_racecourse: Callable = parse_racecourse_p3,
) -> int:
    _, enemy_score = complete_race_p2(
        chariot_input_file, racecourse_input_file, loops, parse_racecourse
    )
    score_to_beat = enemy_score[0][0]
    print(score_to_beat)
    all_combos = set(["".join(p) for p in permutations("+++++---===")])
    total_combos = len(all_combos)
    current_combo = 0
    winning_combo_count = 0
    for combo in all_combos:
        score = complete_race_p2(combo, racecourse_input_file, loops, parse_racecourse)[
            1
        ][0][0]
        if score > score_to_beat:
            winning_combo_count += 1
        current_combo += 1
        if current_combo % 100 == 0:
            print(f"{total_combos - current_combo} remaining!")
    return winning_combo_count


if __name__ == "__main__":
    # part 1

    print(complete_race_p1("day7/day7_inputs/day7_practise_p1.txt", 10))
    print(complete_race_p1("day7/day7_inputs/day7_final_p1.txt", 10))

    # part 2

    print(
        complete_race_p2(
            "day7/day7_inputs/day7_practise_p1.txt",
            "day7/day7_inputs/day7_practise_p2.txt",
            10,
            parse_racecourse_p2,
        )
    )
    print(
        complete_race_p2(
            "day7/day7_inputs/day7_final_chariots_p2.txt",
            "day7/day7_inputs/day7_final_racecourse_p2.txt",
            10,
            parse_racecourse_p2,
        )
    )

    # part 3

    print(
        find_winning_combos(
            "day7/day7_inputs/day7_final_chariots_p3.txt",
            "day7/day7_inputs/day7_final_racecourse_p3.txt",
            2024,
        )
    )
