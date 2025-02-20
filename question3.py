def update_dictionary(dct, key, value):
    keys = dct.keys()
    for k in keys:
        print("Original value of", k, "=", dct[k])
        dct[key] = value
    return dct

dct1 = update_dictionary({}, "name", "Alice")
print(dct1)

dct2 = update_dictionary({"age": 25}, "age", 26)
print(dct2)