example = ['hello', 'world', 'this', 'is', 'an', 'example', 'sentence']

# traditional way
for i in range(len(example)):
    print(i, example[i])

# using enumerate
print('\n')
for ind, val in enumerate(example):
    print(ind, val)
print('\n')

# enumerate using dicts

sample_dict = {1: 'hello', 'second index': 'world', 44: 'sample dict'}

for k, v in enumerate(sample_dict):
    print(v, sample_dict[v])


# turn a list into a dict using enumerate
sample_list = ['first item', 'second item', 'third item', 'fourth item']
new_dict = dict(enumerate(sample_list))
print('\n{}\n{}'.format(sample_list, new_dict))
