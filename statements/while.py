state = 1

while state < 5:
    print(state)
    state += 1
    
    # break, pass, continue
    x = [1,2,3]

for item in x:
    pass

myString = 'Sammy'
    
for letter in myString:
    if letter == 'a':
        continue
    print(letter)

for letter in myString:
    if letter == 'a':
        break
    print(letter)
