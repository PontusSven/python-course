# True
2 == 2
'hello' == 'hello'
3 != 3
2 >= 2


# False
2 == 1
2 == '2'
'hello' == 'bye'
3 < 5

# Mutliple comparisons

2 < 3 < 4
1 < 2 and 2 < 3
2 == 2 or 1 == 1 



""" myString = "Word"
myList = []

for letter in myString:
    myList.append(letter)

print(myList) """

myString = 'Wordtwo'
myList = [letter for letter in myString]
print(myList)