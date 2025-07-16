def get_books_text (filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

from stats import count_words
from stats import count_letters
from stats import sort_dict
import sys

def main ():
    if len(sys.argv) != 2:
        print ("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = get_books_text (path)
    word_count = count_words(text)
    letter_count = count_letters(text)
    sorted_letter_count = sort_dict (letter_count)

    print ("============ BOOKBOT ============")
    print (f"Analyzing book found at {path}...")
    print ("----------- Word Count ----------")
    print (f"Found {word_count} total words")
    print ("--------- Character Count -------")
    for letter in sorted_letter_count:
        print (f"{letter['char']}: {letter['num']}")
    print ("============= END ===============")
main()
