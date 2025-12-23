def number_of_words(text_file):
    num_words = 0
    words = text_file.split()
    for word in words:
        num_words += 1

    print(f"Found {num_words} total words")


def char_dict(text):
    chars = {}

    for char in text:
        lowered = char.lower()
        if lowered.isalpha():  # ignore punctuation and spaces
            chars[lowered] = chars.get(lowered, 0) + 1

    return chars


def sort_on(items):
    return items["num"]


def sorted_dict(char_counts):
    sorted_list = []

    for char, count in char_counts.items():
        sorted_list.append({"char": char, "num": count})

    sorted_list.sort(reverse=True, key=sort_on)

    for item in sorted_list:
        print(f"{item['char']}: {item['num']}")
