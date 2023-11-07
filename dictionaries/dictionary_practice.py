# empty dictionary
artists = {}

# add key-value pairs
artists['name'] = 'Ken Carson'
artists['song'] = 'Overtime'
artists['album'] = 'A Great Chaos'
print(artists)

# modifying values
artists['song'] = "It's over"
print(f"With song modified:\n {artists}")

# removing key-value pair
del artists['album']
print(f"Album removed:\n{artists}")
print(f"\n")

# multiple items, ENTER after {
artist_info = {
    'name': 'Ken Carson',
    'age': 21,
    'location': 'Atlanta',
    'music label': 'Opium',
    'genre': 'Trap',
}
print(artist_info)

# get() method
artist_age = artist_info.get('age')
print(f"We used get method to get the age:\n{artist_age}")

# if key is non-existent, we set default value, otherwise None is the default
artist_racks = artist_info.get('racks', 'we dont have that info')
print(artist_racks)

# loop key-value pairs
print(f"\nDemonstrating key-value looping:\n")
for key, value in artist_info.items():
    print(f"Key: {key}")
    print(f"Value: {value}\n")

print(f"Demonstrating key looping:\n")
# looping through keys
for key in artists.keys():
    print(key.title())
print(f"\nMethod 2:")
for key in artist_info:
    print(key.title())

# ordered loop
print(f"\nSorted:")
for key in sorted(artist_info.keys()):
    print(key.title())

artist_info['age'] = 23
# value looping
print(f"\nValues:")
for value in artist_info.values():
    print(value)

# using dict() method
labels = dict(zip(['Carti', 'Lone', 'Ken', 'Trav', 'Yeat'],
                  ['Opium', 'Opium', 'Opium', 'Cactus', 'Twizzyrich']))
print(f"\nZip mapping:")
print(labels)

# Remove duplicates
# A set is a dictionary w/o keys. Sets do not retain items in any specific order
print(f"\nUnique set:")
for label in set(labels.values()):
    print(label)

# Nesting
# Dictionaries in list
print(f"\ndictionaries in list item:")
all_artists = [artists, artist_info]
print(all_artists)

# List in dict
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'cheese', 'pineapple', 'salami'],
    'sizes': ['small', 'medium', 'large'],
}
print(f"\nList items in dictionary:")
print(pizza)
print(f"You ordered a {pizza['crust']} crust pizza with the toppings:")
for topping in pizza['toppings']:
    print(topping)

# Dictionary in dictionary
print(f"\n Demonstrating dict in dict:")

cats = {
    'Lynx': {
        'Social': 'Medium',
        'Fur': 'Tough',
        'Age': 13,
    },
    'Siamese': {
        'Social': 'High',
        'Fur': 'Softer',
        'Age': 7,
    },
    'Tabby': {
        'Social': 'High',
        'Fur': 'Soft',
        'Age': 5,
    },
}
print(f"{cats}\n")
for cat, cat_info in cats.items():
    print(f"{cat} has the following features:{cat_info}")