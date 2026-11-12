#Enter two different sets, combine them, and remove duplicates

def combine_sets():
    set1 = set(input("Enter elements of first set separated by spaces: ").split())
    set2 = set(input("Enter elements of second set separated by spaces: ").split())

    new_set = set1.union(set2)

    print("First Set:", set1)
    print("Second Set:", set2)
    print("Combined Set without duplicates:", new_set)

combine_sets()
