import regex as re
import numpy as np

def count_runic_words_p1(input_file: str) -> int:
    with open(input_file) as words_and_runes:
        for line in words_and_runes.readlines():
            if match := re.match(r"WORDS:(.*)", line):
                runic_words = match.group(1).split(",")
            elif re.match(r"\w", line):
                sentence = line
    runic_word_count = 0
    for word in runic_words:
        runic_word_count += sentence.count(word)
    return runic_word_count


def count_runic_words_p2(input_file: str) -> int:
    with open(input_file) as words_and_runes:
        sentences = []
        for line in words_and_runes.readlines():
            if match := re.match(r"WORDS:(.*)", line):
                runic_words = match.group(1).split(",")
                runic_words = set(runic_words + [word[::-1] for word in runic_words])
            elif re.match(r"\w", line):
                line = line.strip()
                sentences.append(line)
    runic_words_regex = (
        rf"(?=({("|").join(sorted(runic_words, key=len, reverse=True))}))"
    )
    runic_word_count = 0
    for sentence in sentences:
        matches = re.finditer(runic_words_regex, sentence)
        unique_characters = set()
        for match_found in matches:
            unique_characters.update(
                set(
                    range(
                        match_found.start(),
                        match_found.start() + len(match_found.group(1)),
                    )
                )
            )
        runic_word_count += len(unique_characters)
    return runic_word_count


def get_coords(
    match_indices: set[int], orient: str, coord: int, sentence_length: int
) -> set[tuple[int]]:
    updated_indices = set()
    for index in match_indices:
        if index > sentence_length - 1:
            updated_indices.add(index % sentence_length)
        else:
            updated_indices.add(index)
    if orient == "h":
        return {(coord, match_index) for match_index in updated_indices}
    if orient == "v":
        return {(match_index, coord) for match_index in updated_indices}


def count_runic_words_p3(input_file: str) -> int:
    with open(input_file) as words_and_runes:
        sentences_grid = []
        for line in words_and_runes.readlines():
            if match := re.match(r"WORDS:(.*)", line):
                runic_words = match.group(1).split(",")
                runic_words = set(runic_words + [word[::-1] for word in runic_words])
            elif re.match(r"\w", line):
                line = line.strip()
                sentences_grid.append([*line])
    sentences_grid = np.array(sentences_grid)
    sentence_length = len(sentences_grid[0])
    all_items = []
    for col_index, column in enumerate(sentences_grid.T):
        all_items.append(("".join(column), "v", col_index))
    for row_index, row in enumerate(sentences_grid):
        all_items.append(("".join(row) + "".join(row), "h", row_index))

    runic_words_regex = (
        rf"(?=({("|").join(sorted(runic_words, key=len, reverse=True))}))"
    )
    unique_coords = set()
    for item in all_items:
        sentence, orient, coord = item
        matches = re.finditer(runic_words_regex, sentence)
        unique_characters = set()
        for match_found in matches:
            unique_characters.update(
                set(
                    range(
                        match_found.start(),
                        match_found.start() + len(match_found.group(1)),
                    )
                )
            )
        unique_coords.update(
            get_coords(unique_characters, orient, coord, sentence_length)
        )

    return len(unique_coords)


if __name__ == "__main__":
    # part 1

    print(count_runic_words_p1("day2/day2_inputs/day2_practise_p1.txt"))
    print(count_runic_words_p1("day2/day2_inputs/day2_final_p1.txt"))

    # part 2

    print(count_runic_words_p2("day2/day2_inputs/day2_practise_p2.txt"))
    print(count_runic_words_p2("day2/day2_inputs/day2_final_p2.txt"))

    # part 3
    print(count_runic_words_p3("day2/day2_inputs/day2_practise_p3.txt"))
    print(count_runic_words_p3("day2/day2_inputs/day2_final_p3.txt"))
