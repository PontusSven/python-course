import math  

class Line():

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        dist = math.sqrt((self.coor1[1] - self.coor1[0])**2 + (self.coor2[1] - self.coor2[0])**2)
        print(dist)

    def slope(self):
        m = (self.coor2[1] - self.coor2[0]) / (self.coor1[1] - self.coor1[0])
        print(m)
       
coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1, coordinate2)

class Cylinder():
    pi = 3.14

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        v = Cylinder.pi*(self.radius**2)*self.height
        print(v)

    def surface_area(self):
        area = 2 * Cylinder.pi * (self.radius) * (self.height) + 2 * Cylinder.pi* (self.radius**2)
        print(area)

my_cylinder = Cylinder(2,3)

# Challenge

class BankAccount():
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, deposit):
        self.balance += deposit
        print('Balance is: {}'.format(self.balance))
        

    def withdraw(self, withdraw):

        if withdraw <= self.balance:
            self.balance -= withdraw
            print('Balance is: {}'.format(self.balance))
        else:
            print('You can not withdraw more than your balance')
            print('Your balance is: {}'.format(self.balance))
        

account = BankAccount('Pontus', 100)
account.deposit(50)
account.withdraw(100)
account.withdraw(50)