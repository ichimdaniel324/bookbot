def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = count_words(text)
    print (words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_words(string):
    words =string.split()
    counter = 0
    for word in words:
        counter += 1
    return counter

def count_characters(string):
    lowered_string =string.lower()
     

main()
# main()