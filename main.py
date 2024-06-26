def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = count_words(text)
    number_of_words = f"the book has {words} words"
    character_count = count_characters(text)
    
    char_list = []
    for char, count in character_count.items():
        char_list.append({"char": char, "count": count})
    
    def sort_on(dict):
        return dict["count"]

    char_list.sort(reverse=True, key=sort_on)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{words} words found in the document")
    for item in char_list:
        print(f"The '{item['char']}' character was found {item['count']} times")
    print("--- End report ---")
    

def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_words(string):
    words = string.split()
    counter = 0
    for word in words:
        counter += 1
    return counter

def count_characters(string):
    lowered_string = string.lower()
    char_count = {}
    for char in lowered_string:
        if char.isalpha():  # Check if the character is an alphabet character
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

main()