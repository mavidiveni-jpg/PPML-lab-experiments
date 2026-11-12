#wap to create a dictionary and print the key which has the 
#maximum unique values 
def maximum(d):
    max_key = None
    max_unique = 0

    for key in d:
        unique = len(set(d[key]))

        if unique > max_unique:
            max_unique = unique
            max_key = key

    return max_key


d = eval(input("Enter dictionary: "))

print("Key with maximum unique values:", maximum(d))
