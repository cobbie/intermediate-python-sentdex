# .join()
names = ['Sam', 'Andrea', 'Amira']
nums = [1, 2, 4, 2]
for name in names:
    print(' '.join(['Hello there, ', name]))

print('-'.join(names))

# String concatenation: opening a file
import os

location_of_files = 'C:\\Users\\cobbi\\OneDrive\\Documents\\Python\\Intermediate Python Programming - PPNET'
file_name = 'test.txt'

print(location_of_files + '\\' + file_name)

with open(os.path.join(location_of_files, file_name)) as f:
    print(f.read())

# String concatenation: Pythonic way

# traditional
person = 'Dany'
num = 5

print(person, 'had', num, 'apples')

# Pythonic

print('{} had {} apples'.format(person, num))
