
def generate_name(file, targetName):
    splittedTargetName = targetName.split(" ")
    firstName = splittedTargetName[0].capitalize()
    secondName = splittedTargetName[1].capitalize()
    firstNameFirstLetterPosition = ord( firstName[0] ) - 64
    secondNameFirstLetterPosition = ord( secondName[0] ) - 38
    heroNames = open("FinalProblemSet/nameGenerator/{}".format(file) )
    count = 0
    for name in heroNames:
        count += 1
        if firstNameFirstLetterPosition == count:
            newFirstName = name.strip()
        if secondNameFirstLetterPosition == count:
            newSecondName = name.strip()


    newFullName = "Superhero name for " + targetName + " is " + newFirstName + " " + newSecondName
    return newFullName

# print(generate_name("heronames.txt", "Addison Zook"))
# print(generate_name("heronames.txt", "Uma Irwin"))
# print(generate_name("heronames.txt", "David Joyner"))
print(generate_name("heronames.txt", "Yurii Surnuk"))
print(generate_name("heronames.txt", "Anastasia Kotleta"))







