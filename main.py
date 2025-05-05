from stats import get_book_text,get_num_words,countChar,sortedDict

def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    # Instead of just printing the count, format it as shown in the example
    # Your get_num_words() function currently prints directly, you might want to modify it
    # to return the count instead
    # ...
    
    book_text = get_book_text("books/frankenstein.txt")
    freq = countChar(book_text)
    sorted_chars = sortedDict(freq)
    
    print("--------- Character Count -------")
    # Loop through sorted_chars and print each alphabetical character and its count
    # ...
    
    print("============= END ===============")
main()