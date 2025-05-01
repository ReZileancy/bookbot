def get_book_text(filePath):
    with open(filePath) as file:
        fileContents = file.read()
    return fileContents

def main():
    get_book_text("books/frankenstein.txt")
    