# Write a class named "Phone". The Phone class should
# have an attribute called "storage" which defaults to
# 128, and an attribute called "color" which defaults
# to "red".
#
# Hint: 'attribute' is another common word for
# 'instance variable'.


# Write your class here!
class Phone:
    def __init__(self):
        self.color = 'red'
        self.storage = 128


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print 128 and red, each on a separate line.
new_phone = Phone()
print(new_phone.storage)
print(new_phone.color)


    