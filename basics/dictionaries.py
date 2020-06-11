person = {'name':'Pontus', 'age':27, 'location':'Göteborg'}
print(person['name'])

mylist = {'key':['a','b','c']}

letter = mylist['key'][2].upper()
print(letter)

# add new value
d = {'k1': 100, 'k2':200}
d['k3'] = 300
print(d)

# get keys
d.keys()
# get values
d.values()
# get key and values
d.items()