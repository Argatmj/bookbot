def count_words(text):
    word_count = 0
    words = text.split()
    for word in words:
        word_count +=1
    return word_count

def count_characters(text):
    dict = {}
    words = text.split()
    for word in words:
        for character in word:
            char = character.lower()
            if char not in dict:
                dict[char] = 1
            else:
                dict[char] += 1
    print(dict)




with open("books/frankenstein.txt") as f:
    file_contents = f.read()
count_characters(file_contents)
