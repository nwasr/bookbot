from stats import get_book_text,count_words,count_characters,sort_characters
import sys

def report(filepath,num_words,characters_dict):
    """
    Print filepath, Word count and Character count as report 
    """
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print('----------- Word Count ----------')
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for _ in sort_characters(characters_dict):
        if _[0].isalpha():
            print(f"{_[0]}: { _[1]}") 
    print("============= END ===============")



def main():
    if len(sys.argv)<2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    file_contents = get_book_text(filepath)
    num_words = count_words(file_contents)
    characters_dict = count_characters(file_contents)
    report(filepath,num_words,characters_dict)

main()