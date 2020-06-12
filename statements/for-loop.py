myList = [1,2,3,4,5]
listSum = 0

for item in myList:
    listSum += item
    # check for even
    if item % 2 == 0:
        print('Even number {}'.format(item))
    else:
        print('Odd number {}'.format(item))

    print(listSum)

myString = 'Hello World'

for letter in myString:
    print(letter)

# tuple unpacking
myTuples = [(1,2), (3,4), (5,6)]

for a,b in myTuples:
    print(a)
    print(b)


# loop dictionariesmy

myDictionary = {'k1': 3, 'k2': 6}

# .value()
# .item()
for key, value in myDictionary.items():
    print(key)
    print(value)

word = 'abcde'
for item in enumerate(word):
    print(item)
