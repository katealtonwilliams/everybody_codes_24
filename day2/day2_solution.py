import re

def count_runic_words_p1(input_file: str) -> int:
    with open(input_file) as words_and_runes:
        for line in words_and_runes.readlines():
            if (match := re.match(r"WORDS:(.*)", line)):
                runic_words = match.group(1).split(',')
            elif re.match(r"\w", line):
                sentence = line
    runic_word_count = 0
    for word in runic_words:
        runic_word_count += sentence.count(word)
    return runic_word_count

if __name__ == "__main__":
    
    # part 1
    
    print(count_runic_words_p1('day2/day2_inputs/day2_practise_p1.txt'))
    print(count_runic_words_p1('day2/day2_inputs/day2_final_p1.txt'))