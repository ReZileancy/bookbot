def get_num_words():
    text = get_book_text("books/frankenstein.txt")
    words = text.split()
    wordCount = len(words)
    print(f"Found {wordCount} total words")

def get_book_text(filePath):
    with open(filePath, encoding="utf-8") as file:
        fileContents = file.read()
    return fileContents

def countChar(text):
    freq = {}
    for c in text.lower():
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1
    return(freq)

def sortedDict(dict):
    # Create a list to hold the dictionaries
    chars_list = []
    
    # Convert each character and count into a dictionary and add to the list
    for char, count in dict.items():
        chars_list.append({"char": char, "num": count})
    
    # Sort the list by count (highest to lowest)
    # You'll need a helper function like in the hint
    def sort_on(dict):
        return dict["num"]
    
    chars_list.sort(reverse=True, key=sort_on)
    
    return chars_list