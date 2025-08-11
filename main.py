from stats import get_num_words, get_char_count

def get_book_text(filepath):
    """
    Reads the content of a file and returns it as a string.

    Args:
        filepath (str): The path to the text file.

    Returns:
        str: The contents of the file.
    """
    with open(filepath) as f:
        return f.read()

def main():
    """
    Main function to execute the program.
    It reads the book's text, counts the words and characters, and prints the results.
    """
    # The relative path to the book file.
    book_path = "books/frankenstein.txt"
    
    # Get the book's content as a string
    book_contents = get_book_text(book_path)

    # Count the words in the book's content using the imported function
    num_words = get_num_words(book_contents)

    # Count the character frequency using the new imported function
    char_counts = get_char_count(book_contents)

    # Print the word count to the console
    print(f"{num_words} words found in the document")

    # Print the character count dictionary
    print(char_counts)

# This line ensures the main() function is called when the script is executed
if __name__ == "__main__":
    main()
