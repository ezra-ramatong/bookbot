def main():
    book = "books/frankenstein.txt"
    text = get_book_text(book)
    word_count = get_word_count(text)
    char_dict = get_char_count(text)
    generate_report(word_count, char_dict, book)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_word_count(text):
    words = text.split()
    return len(words)


def get_char_count(text):
    char_count = {}
    for c in text:
        lowered = c.lower()
        char_count[lowered] = char_count.get(lowered, 0) + 1
    return char_count


def generate_report(word_count, char_dict, book):
    print(f"--- Begin report of {book} ---")
    print(f"{word_count} words found in the document\n")
    sorted_char_dict = dict(
        sorted(char_dict.items(), key=lambda item: item[1], reverse=True)
    )

    for k, v in sorted_char_dict.items():
        if k.isalpha():
            print(f"The '{k}' character was found {v} times")

    print("--- End report ---")


main()
