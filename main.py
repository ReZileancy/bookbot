from stats import get_book_text,get_num_words,countChar,sortedDict
import sys

def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    get_num_words()
    
    book_text = get_book_text("books/frankenstein.txt")
    freq = countChar(book_text)
    sorted_chars = sortedDict(freq)
    
    print("--------- Character Count -------")
    # Loop through sorted_chars and print each alphabetical character and its count
    # ...
    
    print("============= END ===============")
main()
