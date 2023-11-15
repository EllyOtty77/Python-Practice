labels = dict(zip(['Carti', 'Lone', 'Ken', 'Trav', 'Yeat'],
                  ['Opium', 'Opium', 'Opium', 'Cactus', 'Twizzyrich']))
print(labels)

for key in labels:
    print(f"{key}: {labels[key]}")


# Filter dictionary
song_counts = dict(zip(['Carti', 'Ken', 'HXG', 'The Neighbourhood', 'Lone', 'Yeat', 'Lucki'],
                      [1, 9, 6, 2, 5, 2, 1]))

print(f"\nMost listened:")
for key in song_counts:
    if song_counts[key] > 3:
        print(key, song_counts[key])

# print(len(song_counts.keys()))

# sorting
print(f"\nSorted:")
lst = list(song_counts.keys())
lst.sort()
for key in lst:
    print(key, song_counts[key])

# update method
song_counts.update({'salvia path': 1})
print(song_counts)

# clear items
song_counts.clear()
print(song_counts)

# passin a list of keys and an initial value for all of the values (the default is None):
value_o = dict.fromkeys(['a', 'b'], 0)
print(value_o)