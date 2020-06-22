x = 25

def printer():
    x = 50
    return x

name = 'THIS IS A GLOBAL STRING'

def greet():

    name = 'Pontus'

    def hello():
        print('Hello ' + name)

    hello()

greet()

age = 27

def sayAge():
    global age
    print('Age is: {}'.format(age))

    age = 'NEW VALUE'
    print('new age is: {}'.format(age))

sayAge()
print(age)

location = 'Gothenburg'

def printLoc(loc):
    return loc

x = printLoc(location)
print('x is now: ' + x)