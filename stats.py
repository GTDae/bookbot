def get_num_words(text):
    """
    Counts the number of words in a given string.

    Args:
        text (str): The string content to analyze.

    Returns:
        int: The number of words in the string.
    """
    words = text.split()
    return len(words)

def get_char_count(text):
    """
    Counts the frequency of each character in a string, ignoring case.

    Args:
        text (str): The string content to analyze.

    Returns:
        dict: A dictionary where keys are lowercase characters and values are their counts.
    """
    chars = {}
    for char in text.lower():
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars