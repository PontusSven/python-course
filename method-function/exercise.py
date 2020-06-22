# write a function that comoutes the volume of a sphere given its radius

pi = 3.1415926535897931

def vol(radius):
    V = 4.0/3.0*pi* radius**3
    return V

sphere = vol(2)

# write a function that checks whether a number is in a given range (inclusive of high and low)

def ran_check(num, low, high):

    if num >= low and num <= high:
        return True
    
    return False

answer = ran_check(1,2,10)

def check_string(word):
    counter = {'upper': 0, 'lower': 0}

    word = word.replace(" ", "")

    letters = [char for char in word]

    print(letters)

    for letter in letters:
        if letter.isupper():
            counter['upper'] += 1
            print(letter + ' is upper')
        else:
            counter['lower'] += 1
            print(letter + ' is lower')

    print('No of Upper case letters: {}'.format(counter['upper']))
    print('No of Lower case letters: {}'.format(counter['lower']))


my_word = 'Hello World'

check_string(my_word)

def unique_list(my_list):
    return set(my_list)

my_list = unique_list([1,1,1,1,2,2,2,3,3,3,4,4,5,5])

def multipy(my_list):
    total = 1

    for num in my_list:
        total = total * num

    return total


answer = multipy([1,2,2])


def palindrome(word):
    text = word[::-1]
    print(text)

palindrome('hello')