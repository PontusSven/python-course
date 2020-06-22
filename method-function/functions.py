
def myfunc(**kwargs):
    if 'fruit' in kwargs:
        print('my fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')

myfunc(fruit='apple')


"""
def summerizer(*args):
    return sum(args)

sum1 = summerizer(1,2,3,4,5)
print(sum1)

# Input
result = input('Enter your age')

print(int(result))

def print_name(name='DEFAULT NAME'):
    return 'Hello' + name

result3 = print_name()
print(result3)
result2 = print_name('Pontus')
print(result2)
"""