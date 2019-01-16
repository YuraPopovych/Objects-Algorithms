
def count_capital_consonants(words):
    vowel = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for word in words:
        if word.isalpha():
            if word.lower() not in vowel and word == word.upper():
                count += 1
    return count

print(count_capital_consonants("Georgia Tech"))
print(count_capital_consonants("GEORGIA TECH"))
print(count_capital_consonants("gEOrgIA tEch"))


