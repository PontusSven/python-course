# sets are unordered lists
# sets can only have unique values
myset = set()
myset.add(1)
myset.add(2)

# cast list to set() to only show unique values
myList = {1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,}
print(set(myList))

myString = "Mississippi"
print(set(myString))