# tuples are immutable lists
t = (3,5)
print(t)

# t[0] = 4
# TypeError: 'tuple' object does not support item assignment
# to change tuple reassign variable
t = (5,9,7)
print(f'reasigned list:\n{t}')

# Nested tuples
T1 = ('Bob', ('dev', 'mgr'))
print(T1)

# Tuple of items in an iterable
T2 = tuple('spamm')
print(T2)
# slice
print(T2[2:])

print(T1+ T2)

# indexing
print(T2.index('p'))

# search
print(T2.count('m'))

# sort
T = ('cc', 'aa', 'dd', 'bb')
# Make a list from a tuple's items
tmp = list(T)
tmp.sort()
print(tmp)

print(sorted(T))

# methods
T = (1, 2, 3, 2, 4, 2)
print(T.index(3))

print(T.count(2))

# one-level-deep immutability
T = (1, [2, 3], 4)
T[1][0] = 'spam'
print(T)

# tuple integrity
bob = dict(name='Bob', age=40.5, jobs=['dev', 'mgr'])
tup = tuple(bob.values())
print(tup)

# Import extension type
from collections import namedtuple
# Make a generated class
Rec = namedtuple('Rec', ['name', 'age', 'jobs'])
# A named-tuple record

bob = Rec('Bob', age=40.5, jobs=['dev', 'mgr'])
print(bob)

# Access by position
print( bob[1])

# Access by attribute
print(bob.age)

# Converting to a dictionary supports key-based behavior when needed
O = bob._asdict()
print(O['name'])

# named tuples are a tuple/class/dictionary hybrid. They also represent
# a classic tradeoff. In exchange for their extra utility, they require extra code
# (the two startup lines in the preceding examples that import the type and make the class),
# and incur some performance costs to work this magic

# named tuples build new classes that extend the tuple type,
# inserting a property accessor method for each named field that maps the name to its position
# and uses formatted code strings instead of class annotation tools like decorators and metaclasses

