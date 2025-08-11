import sys
from stats import get_num_words, get_char_count, get_sorted_char_list

def get_book_text(filepath):
    """
    Reads the content of a file and returns it as a string.
    """
    with open(filepath) as f:
        return f.read()

def main():
    """
    Main function to execute the program.
    """
    # Check if a file path was provided
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    # Get the file path from the command-line arguments
    book_path = sys.argv[1]
    
    # Get the book's content as a string
    book_contents = get_book_text(book_path)

    # Count the words in the book's content
    num_words = get_num_words(book_contents)

    # Count the character frequency
    char_counts = get_char_count(book_contents)

    # Get a sorted list of characters and their counts
    sorted_chars = get_sorted_char_list(char_counts)

    # Print the final report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

# This line ensures the main() function is called when the script is executed
if __name__ == "__main__":
    main()