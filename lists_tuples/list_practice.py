# empty list
a_list = []

items = ['cow', 'cat', 'goat', 'duck', 'lemur', 'panda']
# print(items)

# append list
items.append('sheep')
print(f'appended list: \n {items}')

# pop method
popped_item = items.pop()
print(f'removes last element of list: \n{popped_item}')

popped_index = items.pop(-2)
print(f'remove w index: \n{popped_index}')

# removes an element completely from a list
items.remove('cow')
print(f'list with item removed: \n{items}')

# sorts in ascending order
items.sort()
print(f'list elements sorted in ascending order: \n{items}')

# sort in descending order
items.sort(reverse=True)
print(f'list elements sorted in descending order: \n{items}')

# reverse the sort
items.reverse()
print(f'list order restored: \n{items}')




L = ['abc', 'ABD', 'aBe']
# Sort with mixed case
L.sort()
print(f'mixedcase sort \n: {L}')

# Normalize to lowercase
L.sort(key=str.lower)
print(f'lowercase sort \n: {L}')

# delete statement
cats = ['siamese', 'tabby', 'ginger', 'dark', 'shorthair']
del cats[0]
print(cats)

# list range
num_list = list(range(1,7))
print(f'range generated list: \n{num_list}')

# list comprehension
squares = [value **2 for value in range(1,12,2)]
print(squares)

# slices
dogs = ['husky', 'rott', 'retriever', 'labrador', 'bulldog', 'wild']
print(f'original list:\n{dogs}')
sliced_dogs = dogs[2:5]
print(f'sliced returns up to before specified end index:\n{sliced_dogs}')
sliced_skip = dogs[1:5:3]
print(f'slice and skip items(skips 2):\n{sliced_skip}')

# copy list
duplicate_dogs = dogs[:]
copied_dogs = dogs.copy()
print(f'this list is duplicated:\n{duplicate_dogs}')

# list operations
pets = cats + dogs
print(f'aggregate list:\n{pets}')

cats.extend(['lynx', 'leopard cat', 'wild cat', 'barn cat'])
print(f'extended adds new list to end of list:\n{cats}')

print(f'largest item:\t{max(cats)}')
print(f'length of list:\t{len(cats)}')
print(f'count of items:\t{cats.count("wild cat")}')

# convert string to list
fl = 'county'
str_list = list(fl)
print(f'returns each letter as list:\n{str_list}')

# using split function
str_words = 'Almeda retroville 4u skirt'
spl = str_words.split()
print(f'returns individual words as list:\n{spl}')
# split with delimiter
retro = 'we-was-passing-notes in the-bathroom'
retro_split = retro.split('-')
print(f'split with delmiter(-):\n{retro_split}')

# using join function to make string from list
delimiter = ' '
word = delimiter.join(retro_split)
print(f'string made with join and space delimiter:\n{word}')

# object aliasing
a = ['a', 'c', 'd']
b = a
if a is b:
    print('These are the same')
b[0] = 'sesh'
print(f'list a also changes, multiple referencing:\n{a}')
# always make list copies to avoid aliasing errors

# clear list items
cats.clear()
print(cats)
