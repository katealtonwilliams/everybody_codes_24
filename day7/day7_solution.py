def get_chariot_actions(input_file: str) -> dict[str]:
    chariot_action_map = {}
    with open(input_file) as notes:
        for note in notes.readlines():
            note = note.strip()
            chariot, actions = note.split(":")
            actions = actions.split(",")
            chariot_action_map[chariot] = actions
    return chariot_action_map

def parse_race_course_p1(input_file: str) -> list[str]:
    right_side = ''
    left_side = ''
    with open(input_file) as notes:
        raw_track = notes.readlines()
    top = raw_track[0].strip()[1:]
    bottom = raw_track[-1].strip()[::-1]
    for track_segment in raw_track[1:-1]:
        track_segment = track_segment.split()
        right_side += track_segment[1].strip()
        left_side += track_segment[0].strip()
    return top + right_side + bottom + left_side + '='    
    

def complete_race_p1(input_file: str, rounds: int) -> str:
    chariot_action_map = get_chariot_actions(input_file)
    final_scores = []
    for chariot, actions in chariot_action_map.items():
        current_round = 0
        current_power_level = 10
        total_power_level = 0
        while current_round < rounds:
            current_action = actions[current_round%len(actions)]
            if current_action == "+":
                current_power_level += 1
            if current_action == "-":
                if current_power_level > 0:
                    current_power_level -= 1
            total_power_level += current_power_level
            current_round += 1
        final_scores.append((total_power_level, chariot))
    final_scores.sort(reverse=True)
    final_standings = ''
    for chariot, power_level in final_scores:
        final_standings += power_level
    return final_standings


def complete_race_p2(chariot_input_file: str, racecourse_input_file: str, loops: int) -> str:
    chariot_action_map = get_chariot_actions(chariot_input_file)
    racecourse = parse_race_course_p1(racecourse_input_file)
    final_scores = []
    for chariot, actions in chariot_action_map.items():
        current_loop = 0
        current_power_level = 10
        total_power_level = 0
        current_round = 0
        while current_loop < loops:
            current_action = actions[current_round%len(actions)]
            current_track = racecourse[current_round%len(racecourse)]
            if current_track == "+" or current_track == '=' and current_action == '+':
                current_power_level += 1
            if current_track == "-" or current_track == '=' and current_action == '-':
                if current_power_level > 0:
                    current_power_level -= 1
            total_power_level += current_power_level
            if (current_round + 1) % len(racecourse) == 0:
                current_loop += 1
            current_round += 1
        final_scores.append((total_power_level, chariot))
    final_scores.sort(reverse=True)
    final_standings = ''
    for chariot, power_level in final_scores:
        final_standings += power_level
    return final_standings

if __name__ == "__main__":
    
    # part 1
    
    # print(complete_race_p1("day7/day7_inputs/day7_practise_p1.txt", 10))
    # print(complete_race_p1("day7/day7_inputs/day7_final_p1.txt", 10))

    # part 2
    
    print(complete_race_p2("day7/day7_inputs/day7_practise_p1.txt", "day7/day7_inputs/day7_practise_p2.txt", 10))
    print(complete_race_p2("day7/day7_inputs/day7_final_chariots_p2.txt", "day7/day7_inputs/day7_final_racecourse_p2.txt", 10))