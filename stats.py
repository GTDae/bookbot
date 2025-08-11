def get_num_words(text):
    """
    Counts the number of words in a given string.
    """
    words = text.split()
    return len(words)

def get_char_count(text):
    """
    Counts the frequency of each character in a string, ignoring case.
    """
    chars = {}
    for char in text.lower():
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def get_sorted_char_list(char_counts):
    """
    Converts a character count dictionary into a sorted list of dictionaries.
    """
    sorted_list = []
    for char, count in char_counts.items():
        if char.isalpha():
            sorted_list.append({"char": char, "num": count})
    
    # Sort the list by the "num" key in descending order
    sorted_list.sort(reverse=True, key=lambda item: item["num"])
    return sorted_list