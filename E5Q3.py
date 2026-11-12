#wap to enter a dictonary and remove the duplicate values inside the dictionary
def remove_duplicate(d):
    d1 = {}

    for key in d:
        if d[key] not in d1.values():
            d1[key] = d[key]

    return d1


d = eval(input("Enter dictionary: "))

print("Dictionary after removing duplicate values:")
print(remove_duplicate(d))

    