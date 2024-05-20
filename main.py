with open("./books/frankenstein.txt") as f:
    file_contents = f.read()

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    get_num_letters(text)
    print(f"{num_words} words found in the document")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_letters(text):
    count = {"a":0, "b":0, "c":0,
             "d":0, "e":0, "f":0,
             "g":0, "h":0, "i":0,
             "j":0, "k":0, "l":0,
             "m":0, "n":0, "o":0,
             "p":0, "q":0, "r":0,
             "s":0, "t":0, "u":0,
             "v":0, "w":0, "x":0,
             "y":0, "z":0
             }
    low_string = text.lower()
    for l in low_string:
        if l == "a":
            count["a"] += 1
        if l == "b":
            count["b"] += 1
        if l == "c":
            count["c"] += 1
        if l == "d":
            count["d"] += 1
        if l == "e":
            count["e"] += 1
        if l == "f":
            count["f"] += 1
        if l == "g":
            count["g"] += 1
        if l == "h":
            count["h"] += 1
        if l == "i":
            count["i"] += 1
        if l == "j":
            count["j"] += 1
        if l == "k":
            count["k"] += 1
        if l == "l":
            count["l"] += 1
        if l == "m":
            count["m"] += 1
        if l == "n":
            count["n"] += 1
        if l == "o":
            count["o"] += 1
        if l == "p":
            count["p"] += 1
        if l == "q":
            count["q"] += 1
        if l == "r":
            count["r"] += 1
        if l == "s":
            count["s"] += 1
        if l == "t":
            count["t"] += 1
        if l == "u":
            count["u"] += 1
        if l == "v":
            count["v"] += 1
        if l == "w":
            count["w"] += 1
        if l == "x":
            count["x"] += 1
        if l == "y":
            count["y"] += 1
        if l == "z":
            count["z"] += 1        
    
    print(count)
main()
