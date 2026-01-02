import sys
from stats import get_word_count
from stats import per_letter_count
from stats import sorting_dictionaries


def main():
    # print(get_book_text(filepath))
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    text = get_book_text(filepath)
    num_words = get_word_count(text)
    dictionary_letter = per_letter_count(text)
    sorted_list = sorting_dictionaries(dictionary_letter)
    print("============== BOOKBOT ==============")
    print(f"Analyzing book found at {filepath}...")
    print("------------ Word Count -------------")
    print(f"Found {num_words} total words") 
    print("---------- Character Count -----------")
    for item in sorted_list:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============== End ================")

def get_book_text(filepath):
    with open(filepath, 'r') as f: 
        file_contents = f.read()
        file_contents = file_contents
    return file_contents

main()

