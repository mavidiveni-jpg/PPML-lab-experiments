#Enter two sets and perform all set operations
def set_operations():
    set1 = set(input("Enter elements of first set separated by spaces: ").split())
    set2 = set(input("Enter elements of second set separated by spaces: ").split())

    print("Set 1:", set1)
    print("Set 2:", set2)

    print("Union:", set1 | set2)
    print("Intersection:", set1 & set2)
    print("Difference (Set1 - Set2):", set1 - set2)
    print("Difference (Set2 - Set1):", set2 - set1)
    print("Symmetric Difference:", set1 ^ set2)

set_operations()
