from stats import get_num_words, count_characters, sort_dictionary
import sys


def get_book_text(filepath):
    with open (filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]

    book_text = get_book_text(filepath)

    num_words = get_num_words(book_text)
    print(f"Found {num_words} total words")

    
    char_count = count_characters(book_text)
    
    sorted_dictionary = sort_dictionary(char_count)
    

    for char_dict in sorted_dictionary:
        print(f"{char_dict['characters']}: {char_dict['count']}")
        print("\n")

    


if __name__ == "__main__":
    main()