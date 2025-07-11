def get_book_text(filepath):
    """
    Read the content of file and return as string

    Parameters:
        filepath(path): The path of the book file
    
    Returns:
        str: The content of file as string
    """
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def count_words(book_content):

    """
    Count the number of words in a book.

    Parameters:
        book_content: The content of the book as a string.

    Returns:
        int: The numbers of words in the book.
    """
    return len(book_content.split())

def count_characters(book_content):
    """
    Count the characters(including spaces and symbols) that appear in the book content.

    Parameters:
        book_content: The content of the book as a string.
    
    Returns:
        dict: A dictionary where keys are characters (str) and values are their counts (int).
    """

    book_content_lower_char = book_content.lower()
    characters_dict = {}

    for i in book_content_lower_char:
        if i not in characters_dict:
            characters_dict[i] = 1
        else :
            characters_dict[i] += 1

    return characters_dict

def sort_characters(characters_dict):
    """
    Takes the dictionary of characters and their counts and returns a sorted list of dictionaries.
    """

    return sorted(characters_dict.items(),key = lambda x : x[1],reverse = True)