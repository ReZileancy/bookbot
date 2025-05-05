from stats import get_book_text,get_num_words,countChar

def main():
     get_num_words()
     freq = countChar(get_book_text("books/frankenstein.txt"))
     print(freq)
    

main()