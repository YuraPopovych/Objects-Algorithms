def alter_list(words, indexes):
    for index in indexes:
        word = words[index]
        if word == word.upper():
            words[index] = word.lower()
        if word == word.lower():
            words[index] = word.upper()
    return words

print(alter_list(["hello", "WORLD", "HOW", "are", "you"], [0, 2]))
print(alter_list(["hello", "WORLD", "HOW", "are", "you"], [0, 2, 2]))



