from stats import number_of_words
from stats import char_dict
from stats import sorted_dict
import sys


def get_books_text(file):
    file_content = ""
    with open(file) as f:
        file_content = f.read()
    return file_content


def main():
    file = ""
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file = get_books_text(sys.argv[1])

    number_of_words(file)
    chars = char_dict(file)
    sorted_dict(chars)


main()
