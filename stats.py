def count_words (text):
    words_table = text.split()
    return len(words_table)

def count_letters(text):
    text=text.lower()
    letter_count = {}
    for i in range(0, len(text)):
        if text[i] not in letter_count:
            letter_count[text[i]] = 1
        else:
            letter_count[text[i]]+=1
    return letter_count

def sort_on (list):
    return list["num"]

def sort_dict(dictionary):
    sorted_dictionary = []
    for letter in dictionary:
        if letter.isalpha():
            sorted_dictionary.append({"char": letter, "num": int(dictionary[letter])})
    sorted_dictionary.sort(reverse=True, key=sort_on)

    return sorted_dictionary