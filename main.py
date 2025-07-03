from stats import get_book_text,get_num_words,countChar,sortedDict
import sys

def main():
    if len(sys.argv) == 2:
        book_text = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    print("============ BOOKBOT ============")
    print("Analyzing book found at " + book_text + " ...")
    print("----------- Word Count ----------")
    get_num_words(book_text)
    
    freq = countChar(book_text)
    sorted_chars = sortedDict(freq)
    
    print("--------- Character Count -------")
    # Loop through sorted_chars and print each alphabetical character and its count
    # ...
    
    print("============= END ===============")
main()
