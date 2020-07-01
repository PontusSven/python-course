class Dog():

    # global object attribute
    # same for any instance
    species = 'mamal'
    
    def __init__(self, breed, name, spots, age):
        # expected string
        self.breed = breed
        self.name = name

        # expected int
        self.age = age

        # expected boolean
        self.spots = spots

    def bark(self):
        print('WOOF my name is {}'.format(self.name))

    def calc_age(self):
        return self.age * 7

class Circle():

    pi = 3.14

    def __init__(self, radius=1):
     self.radius = radius
     self.area = radius*radius*Circle.pi

    def get_circumferance(self):
        return self.radius * Circle.pi * 2



my_dog = Dog(breed="Jack Russel", name="Ebba", spots=True, age=5)

my_circle = Circle(30)
print(my_circle.radius) 


