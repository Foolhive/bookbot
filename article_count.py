def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_dict = get_character_count(text)
    chardictlist = chardict_to_listchardict(char_dict)
    chardictlist.sort(reverse=True, key=sort_in)
    art_count_list = get_art_count(text)
    art_count_list.sort(reverse=True, key=sort_in_art)
    print(f"--- Beginning of report for {book_path} ---")
    print(f"{num_words} words were found in the document.")
    for char in chardictlist:
        if char["Character"].isalpha():
            print (f"The character '{char["Character"]}' was found {char["Number"]} times.")
    get_art_count(text)
    for art in art_count_list:
        print(f"The article '{art["Article"]}' was found {art["Number"]} times.")
    print(f"---End of report for {book_path}---")

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

def get_art_count(text):
    lowwords = text.lower()
    lowered_words = lowwords.split()
    art_count = {"the":0, "a":0, "an":0}
    art_count_list = []
    for word in lowered_words:
        if word == "the":
            art_count["the"] += 1
        elif word == "a":
            art_count["a"] += 1
        elif word == "an":
            art_count["an"] += 1
        else:
            pass
    for art in art_count:
        number = art_count[art]
        art_count_list.append({"Article":art, "Number":number})
    return art_count_list


def sort_in_art(art_count_list):
    return art_count_list["Number"]

main()