
def joynernacci(index_number):
    if index_number <= 2:
        return 1
    if index_number % 2 == 0:
        return joynernacci(index_number - 1) + joynernacci(index_number - 2)
    if index_number % 2 != 0:
        return joynernacci(index_number - 1) - joynernacci(index_number -2)


print(joynernacci(5))
print(joynernacci(12))



