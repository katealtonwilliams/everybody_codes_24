import regex as re


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
                print(runic_words)
            elif re.match(r"\w", line):
                line = line.strip()
                sentences.append(line)
    print(sentences)
    runic_words_regex = rf"(?=({("|").join(runic_words)}))"
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


if __name__ == "__main__":
    # part 1

    print(count_runic_words_p1("day2/day2_inputs/day2_practise_p1.txt"))
    print(count_runic_words_p1("day2/day2_inputs/day2_final_p1.txt"))

    # part 2

    print(count_runic_words_p2("day2/day2_inputs/day2_practise_p2.txt"))
    print(count_runic_words_p2("day2/day2_inputs/day2_final_p2.txt"))
