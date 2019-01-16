
def are_anagrams(string1, string2):
    list_for_strings = [string1, string2]
    list_for_string1 = []
    list_for_string2 = []
    count = 0
    for string in list_for_strings:
        count += 1
        for word in string:
            if word == " ": continue
            if count == 1:
                list_for_string1.append(word.lower())
            else:
                list_for_string2.append(word.lower())
    return sorted(list_for_string1) == sorted(list_for_string2)


print(are_anagrams("Elvis", "Lives"))
print(are_anagrams("Elvis", "Live Viles"))
print(are_anagrams("Eleven plus two", "Twelve plus one"))
print(are_anagrams("Nine minus seven", "Five minus three"))



