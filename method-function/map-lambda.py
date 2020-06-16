#lambda expression
mynums2 = [1,2,3,4,5,6,7,8]

square2 = lambda num: num ** 2
lambdaList = list(map(lambda num:num**2, mynums2))
print(lambdaList)

#filter
mynums = [1,2,3,4,5,6,7,8]

def check_even(num):
    return num % 2 == 0

filtered = filter(check_even, mynums)
print(filtered)


# map
def square(num):
    return num**2

my_nums = [1,2,3,4,5]

for item in map(square, my_nums):
    print(item)

list(map(square, my_nums))

def splicer(mystring):
    if len(mystring) % 2 == 0:
        return 'EVEN'
    else:
        return mystring[0]

names = ['Pontus', 'Ebba', 'Kajsa']

result = splicer(names)
print(list(map(splicer, names)))