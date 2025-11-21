from stats import number_of_words
from stats import char_dict
def get_books_text(file):
    file_content = ""
    with open(file) as f:
        file_content = f.read()
    return file_content


def main():
    file = ""
    file = get_books_text("books/frankenstein.txt")

    number_of_words(file)
    char_dict(file) 


main()
