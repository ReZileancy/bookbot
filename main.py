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
    
    bookContent = get_book_text(book_text)
    get_num_words(bookContent)
    
    freq = countChar(bookContent)
    sorted_chars = sortedDict(freq)
    
    print("--------- Character Count -------")
    for chars in sorted_chars:
        if chars["char"].isalpha() == True:
            ch = chars["char"]
            nu = chars["num"]
            print f("{ch}:{nu}")
    
    print("============= END ===============")
main()
