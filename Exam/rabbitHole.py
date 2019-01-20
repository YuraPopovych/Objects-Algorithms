

def rabbit_hole(data_set, target_string):
    try:
        if type(target_string) == list:
            previous_key = target_string[0]
            target_string = target_string[-1]
            if previous_key == data_set[target_string]:
                return False

        key_value = []
        key_value.append( target_string )
        key_value.append( data_set[target_string] )
        return rabbit_hole(data_set, key_value)
    except KeyError:
        return target_string

        

d = {"bat": "pig", "pig": "cat", "cat": "dog", "dog": "ant",
     "cow": "bee", "bee": "elk", "elk": "fly", "ewe": "cod",
     "cod": "hen", "hog": "fox", "fox": "jay", "jay": "doe",
     "rat": "ram", "ram": "rat"}

print(rabbit_hole(d, "bat"))
print(rabbit_hole(d, "ewe"))
print(rabbit_hole(d, "jay"))
print(rabbit_hole(d, "yak"))
print(rabbit_hole(d, "rat"))


