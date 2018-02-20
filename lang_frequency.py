import string
import argparse
import os.path
from collections import Counter


def load_lines_list_from_file(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        return file.readlines()


def find_words(lines_list):
    word_hyphenation = None
    for line in lines_list:
        line = line.strip()
        if line:
            if word_hyphenation:
                line = "{}{}".format(word_hyphenation, line)
            words_in_line = line.split()
            if words_in_line[-1].endswith("-"):
                word_hyphenation = words_in_line[-1][:-1]
                splitted_words_in_line = words_in_line[:-1]
            else:
                word_hyphenation = None
                splitted_words_in_line = words_in_line
            for word in splitted_words_in_line:
                yield word


def get_words_list(raw_lines):
    parsed_words_list = []
    words = find_words(raw_lines)
    for word in words:
        word = word.lower().strip(string.punctuation)
        parsed_words_list.append(word)
    return parsed_words_list


def get_most_frequent_words(words_list, top_limit=10):
    words_counter = Counter(words_list)
    return words_counter.most_common(top_limit)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--filepath", help="Path to txt file")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    if os.path.isfile(args.filepath):
        lines_list = load_lines_list_from_file(args.filepath)
        words_list = get_words_list(lines_list)
        most_frequent_words = get_most_frequent_words(words_list)
        print("most frequent words:")
        for word, count in most_frequent_words:
            print("{} - {} times".format(word, count))
    else:
        print("filepath not found")
