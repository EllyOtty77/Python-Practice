# tuples are immutable lists
t = (3,5)
print(t)

# t[0] = 4
# TypeError: 'tuple' object does not support item assignment
# to change tuple reassign variable
t = (5,9,7)
print(f'reasigned list:\n{t}')