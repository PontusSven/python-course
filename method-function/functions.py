# Input
result = input('Enter your age')

print(int(result))

def print_name(name='DEFAULT NAME'):
    return 'Hello' + name

result = print_name()
print(result)
result2 = print_name('Pontus')
print(result2)