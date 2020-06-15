

# FizzBuzz
for num in range(1,101):
    if num%3 == 0 and num%5 == 0:
        print('FizzBuzz')
    elif num%3 == 0:
        print('Fizz')
    elif num%5 == 0:
        print('Buzz')
    else:
        print(num)
    

"""

st = 'Print every word in this sentence that has an een number of letters'

splitList = st.split()

for word in splitList:
    if len(word) % 2 == 0:
        print('even ' + word)


st = 'Print only the words that start with s in this sentence'

splitted = st.split()

print(splitted)

for word in splitted:
    if word[0] == 's':
        print(word)
    
for num in range(0,11):
    if num % 2 == 0:
        print(num)

myList = [num for num in range(0,50) if num % 3 == 0]

print(myList)

"""