


def sort_with_merge(lst):
    if len(lst) <= 1:
        return lst
    else:
        midpoint = len(lst) // 2
        left = sort_with_merge(lst[:midpoint])
        right = sort_with_merge(lst[midpoint:])
        newlist = []
        while len(left) and len(right) > 0:
            if left[0] > right[0]:
                newlist.append(left[0])
                del left[0]
            else: 
                newlist.append(right[0])
                del right[0]
        newlist.extend(left)
        newlist.extend(right)
        return newlist
print(sort_with_merge([1, 3, -1, -3, -5, 5]))


