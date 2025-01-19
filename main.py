def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_dict = get_character_count(text)
    chardictlist = chardict_to_listchardict(char_dict)
    chardictlist.sort(reverse=True, key=sort_in)
    print(f"{num_words} words found in the document")
    print(f"--- Begin report of frankenstein.txt ---")
    for char in chardictlist:
        if char["Character"].isalpha():
            print (f"The character '{char["Character"]}' was found {char["Number"]} many times.")

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_character_count(text):
    lowered_text = list(text.lower())
    character_count = {}
    for char in lowered_text:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    return character_count

def chardict_to_listchardict(char_dict):
    chardictlist = []
    for char in char_dict:
        number = char_dict[char]
        chardictlist.append({"Character":char,"Number":number})
    return chardictlist

def sort_in(chardictlist):
    return chardictlist["Number"]

main()

