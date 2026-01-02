# Bootdev BookBot Project
import sys
from stats import get_word_count, get_num_char, get_sorted_dicts

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents

def print_report(filepath):
    file_contents = get_book_text(filepath)
    word_count = get_word_count(file_contents)
    sorted_counts = get_sorted_dicts(file_contents)
    counts_string = ""
    for d in sorted_counts:
        counts_string += f"{d["char"]}: {d["num"]}\n"

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    print(counts_string[:-1:])
    print("============= END ===============")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    print_report(filepath)

main()