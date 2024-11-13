def create_branch_map(input_file: str) -> dict[str]:
    tree_map = {}
    fruit_number = 1
    with open(input_file) as notes:
        for note in notes.readlines():
            note = note.strip()
            branch, connections = note.split(":")
            connections = connections.split(",")
            if "@" in connections:
                connections = list(
                    map(lambda x: x.replace("@", f"@{fruit_number}"), connections)
                )
                fruit_number += 1
            for connection in connections:
                tree_map.setdefault(connection, branch)
    return tree_map


def find_unique_path(input_file: str, first_character: bool = False) -> str:
    path_map = create_branch_map(input_file)
    all_paths = {}
    for node in path_map.keys():
        if node.startswith("@"):
            found_bug = False
            full_path = "@"
            path_length = 0
            while node != "RR":
                node = path_map[node]
                full_path = node[0] + full_path if first_character else node + full_path
                path_length += 1
                if node == "ANT" or node == "BUG":
                    found_bug = True
                    break
            if found_bug == True:
                continue
            all_paths.setdefault(path_length, []).append(full_path)
    for paths in all_paths.values():
        if len(paths) == 1:
            return paths[0]


if __name__ == "__main__":
    # part 1

    print(find_unique_path("day6/day6_inputs/day6_practise_p1.txt"))
    print(find_unique_path("day6/day6_inputs/day6_final_p1.txt"))

    # part 2

    print(find_unique_path("day6/day6_inputs/day6_final_p2.txt", True))

    # part 3

    print(find_unique_path("day6/day6_inputs/day6_final_p3.txt", True))
