name = "Pontus"
print(name[2])
slice_name = slice(name[0], name[3])

mystring = "abcdefghijk"
print(mystring)
print(mystring[:3])
print(mystring[3:6])
# every second character
print(mystring[::2])
# reverse string by index
print(mystring[::-1])

# Immutability
letter = "z"
print(letter * 10)
name = "Sam"
print(name.upper())

#split() no parameter splits by whitespace
x = "Hello Word"
print(x.split("l"))

# .format() 3 ways to do
print("Hello my name is {} and I am {} years old".format("Pontus", 27))
print("The {0} {2} {1}".format("fox", "fast", "is"))
print("The {f} {d} {b}".format(f="fox", b="fast", d="is"))

#float formatting
result = 100 / 777
print("the result was {r:1.5f}".format(r = result))

# f string literal
name = "Jose"
age = 34
print(f"His name is {name} and he is {age} years old")










