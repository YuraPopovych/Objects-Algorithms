# Implement insertion sort below.
# Write your code here!
def insertion(my_list):
    sorted_list = []
    for i in range(len(my_list)):
        outer_element = my_list[i]
        if len(sorted_list) == 0:
            sorted_list.append(outer_element)
        else:
            min_element_index = len(sorted_list) 
            for j in range(len(sorted_list)):
                sorted_index = - (1 + j)
                sorted_element = sorted_list[sorted_index]
                if outer_element < sorted_element:
                    min_element_index = sorted_index     
            sorted_list.insert(min_element_index,outer_element)
    return sorted_list        

print(insertion([5, 1, 3, 2, 4]))
print(insertion([28, 20, 10, 11, 5, 32, 36, 15]))
print(insertion([7, 49, 30, 43, 23, 50, 46, 8, 1, 17, 20, 21]))

