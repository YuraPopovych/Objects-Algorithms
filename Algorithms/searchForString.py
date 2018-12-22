

def search_for_string(source, target):
    count = 0
    result = []
    for i in source:
        if str(i) == str(target):
            result.append(count)
        count += 1
    return result        


sample_list = ["artichoke", "turnip", "tomato", "potato", "turnip", "turnip", "artichoke"]
print(search_for_string(sample_list, "turnip"))

