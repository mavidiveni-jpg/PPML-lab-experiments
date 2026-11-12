#wap to input two dictionaries and print the valuesby merging the 
# two dictionaries
# Input two dictionaries

def merge(dict1, dict2):
    dict3 = {**dict1, **dict2}
    print("Values of merged dictionary:")
    print(dict3.values())


dict1 = eval(input("Enter first dictionary: "))
dict2 = eval(input("Enter second dictionary: "))

merge(dict1, dict2)
