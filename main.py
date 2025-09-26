import sys
from stats import count_words
from stats import count_all_letters
from stats import print_report

def get_book_text(path):
    with open(path) as f:
        book_text = f.read()
        return book_text

def main():
    if len(sys.argv) < 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    run_bookbot_report(sys.argv[1])

def run_bookbot_report(book):
    book_text = get_book_text(book)
    letter_count = count_all_letters(book_text)
    sorted_letter_list = print_report(letter_count)

    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print(f"----------- Word Count ----------")
    print(f"Found {count_words(book_text)} total words")
    print(f"--------- Character Count -------")
    for letter in sorted_letter_list:
        print(f"{letter["char"]}: {letter["num"]}")
    print("============= END ===============")

main()
