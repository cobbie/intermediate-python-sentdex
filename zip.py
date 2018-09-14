# zip function: takes elements from mult iterables
# and aggregates into 1 to share index value

x = [1, 2, 3, 4]
y = [7, 6, 2, 6]
z = ['herhe', 'asdfasdf', 'helloworld', '4th']

# zipping into tuples
for zipd in zip(x, y, z):
    print(zipd)

# zip creates zip objects
print(zip(x, y))

# getting the values of zipped objects
for a, b, c in zip(x, y, z):
    print(a, b, c)

# creating a list
list_zipped = list(zip(x, y, z))
print(list_zipped)

# creating a dict
print(dict(zip(x, z)))

# list comprehension
list_comp = [(a, b, c) for a, b, c in zip(x, y, z)]

print(list_comp)
