# Create a list and perform append, insert, remove, pop, sort, reverse, slicing, and iteration operations.
l = [2, 3, 4]

l.append(10)
l.append(30)
l.append(30)
l.append(40)
l.append(50)
l.insert(0, 20)
l.remove(10)
l.pop()
l.sort()
l.reverse()
print(l[1:3])
for i in range(len(l)):
    print(l[i])

for num in l:
    print(num)

# 2. Create a tuple and demonstrate indexing, slicing, unpacking, and immutability.
t = tuple([1,2,3,4]) # or t = () or t = (1,3) or t = 1,2,3

print(t[1])
print(t[1:3])
a, b ,c, d = t
print(a, b, c, d)

t[1] = 5    # immutability, once created cannont change


# 3.Create a set and perform union, intersection, difference, symmetric difference, and subset operations.
set_a = {1,2,3,4,5}
set_b = {4,5,6,7,8}

# union
print(set_a.union(set_b))
print(set_a | set_b)

# intersection
print(set_a.intersection(set_b))
print(set_a & set_b)

# difference
print(set_a.difference(set_b))
print(set_a - set_b)

# symmetric difference
print(set_a.symmetric_difference(set_b))
print(set_a ^ set_b)


#4. Create a dictionary and perform add, update, delete, lookup, iteration, and nested dictionary operations.
d = {'a': 1, 'b': 2, 'c': 3}

# add
d['d'] = 4

# update
d['b'] = 5

# delete

del d['b']    # delete based on key

print(d.pop('c'))   # delete based on key

print(d.popitem())  # delete last key

# lookup
print(d['a'])     # unsafe, if key not exist then it will throw error
print(d.get('a', 'not found')) # safe


for key in d:
    print(key, '->', d[key])


for key in d.keys():
    print(key)

for key, value in d.items():
    print(key,value)

for value in d.values():
    print(value)

prices = {"apple": 100, "banana": 40, "cherry": 200}
multiply_by_2 = {key: value * 2 for key, value in prices.items()}
print(multiply_by_2)

employees = {
    "emp1": {"name": "Arjun", "role": "Developer", "skills": ["Python", "SQL"]},
    "emp2": {"name": "Priya", "role": "Designer", "skills": ["Figma", "CSS"]}
}

print(employees['emp1']['role'])
print(employees['emp1']['skills'][0])


# Reverse a string without using built-in reverse().

p = 'apple'

# solution 1
l = list(p)

left = 0
right = len(l) - 1

while left < right:
    l[left], l[right] = l[right], l[left]
    left += 1
    right -= 1

print(''.join(l))

# solution 2

print(p[::-1])

# solution 3

rev = ''

for i in range(len(p)-1, -1 , -1):
    rev += p[i]
print(rev)


# Check whether a string is a palindrome.
s = 'madam'

print(s == s[::-1])

# Count the frequency of each character in a string.
st = 'little'

d = {}

for ch in st:
    d[ch] = d.get(ch, 0) + 1

print(d)

# Find duplicate elements in a list.

a = [1, 2, 3, 4, 1, 2, 5, 3, 6]

unique = []
duplicate = []

for num in a:
    if num in unique and num not in duplicate:
        duplicate.append(num)
    else:
        unique.append(num)

print(duplicate)

# Remove duplicates from a list while preserving order.
a = [1,2,3,4,1,2,5,3,6]

unique = []

for num in a:
    if num not in unique:
        unique.append(num)

for i in  range(len(unique)):
    a[i] = unique[i]


print(a[:len(unique)])

# Find the second-largest number in a list.
a = [10,32,88,92,65]

largest = float('-inf')
second_largest = float('-inf')

for num in a:
    if num >= largest:
        second_largest = largest
        largest = num
    elif num >= second_largest and num != largest:
        second_largest = num

print(second_largest)

# Find common elements between two lists.
for i in a:
    if i in b:
        print(i)

# Merge two dictionaries.
a = {'a': 1, 'b': 2}
b = {'c':3, 'd': 4}

print({**a, **b})

# Sort a dictionary by keys and values.
a = {'d': 3, 'b': 1, 'c': 2}

d = {key: a[key] for key in sorted(a)}

print(d)