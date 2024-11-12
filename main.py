def count_words(text):
    return len(text.split())

def count_characters(text):
    char_count = {}
    words = text.split()
    for word in words:
        for character in word:
            char = character.lower()
            if char not in char_count:
                char_count[char] = 1
            else:
                char_count[char] += 1
    list_of_dicts = list({key : value} for key, value in char_count.items())
    return list_of_dicts

def sort_on(char_dict):
    return list(char_dict.values())[0]

def print_report(word_count, char_list,book):
    char_list.sort(reverse=True,key=sort_on)
    print(f"--- Begin report of {book} ---")
    print(f"{word_count} words found in the document\n")
    for char_dict in char_list:
        for char in char_dict:
            if char.isalpha():
                print(f"The '{char}' was found {char_dict[char]} times")
    print("--- End report ---")

def main():
    book = "books/frankenstein.txt"
    with open(book) as f:
        file_contents = f.read()
    count = count_words(file_contents)
    char_list = count_characters(file_contents)
    print_report(count,char_list,book)

if __name__ == "__main__":
    main()