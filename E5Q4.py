#wap to enter a set and copy the content of the set into a new set one element at a time
def copy_set(s):
    s1 = set()

    for i in s:
        s1.add(i)

    return s1


s = eval(input("Enter a set: "))

print("New set:", copy_set(s))

