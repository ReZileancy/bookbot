def get_book_text(filePath):
    with open(filePath, encoding="utf-8") as file:
        fileContents = file.read()
    return fileContents

def main():
    text = get_book_text("books/frankenstein.txt")
    print(text)

main()