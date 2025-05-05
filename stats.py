def get_num_words():
    text = get_book_text("books/frankenstein.txt")
    words = text.split()
    wordCount = len(words)
    print(f"{wordCount} words found in the document")

def get_book_text(filePath):
    with open(filePath, encoding="utf-8") as file:
        fileContents = file.read()
    return fileContents