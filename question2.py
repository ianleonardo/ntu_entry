def find_and_replace(lst, find_val, replace_val):
    if not type(lst) is list:
        return -1

    for i in range(len(lst)):
        if lst[i] == find_val:
            lst[i] = replace_val

    return lst

print(find_and_replace ([1, 2, 3, 4, 2, 2], 2, 5))
print(find_and_replace(["apple", "banana", "apple"], "apple", "orange"))
