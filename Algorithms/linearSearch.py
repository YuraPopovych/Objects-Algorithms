
def linear(a_list, element_to_find):
    count = 0
    for element in a_list:
        if element == element_to_find:
            return count
        count += 1
    return False

a_list = [5, 1, 3, 6, 7, 3, 1, 6, 7, 8, 3, 6]
print(linear(a_list, 6))



