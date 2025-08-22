import sys
from stats import word_count, character_count, sort_the_dict_list

def get_book_text(filepath: str):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
        

def main():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
    
    text = get_book_text(book_path)
    count = word_count(text)
    characters = character_count(text)
    #sorted_char_count = sort_the_dict_list(characters)
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")

    sorted_char_count = sort_the_dict_list(characters)

    for char in sorted_char_count:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")

    print("============= END ===============")

    


main()