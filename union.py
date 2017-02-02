# file name: union.py
# author: Ben Silbernagel
# created: 4/19/2016
# class: Intro to Computer Science, by Udacity
# purpose: joins two lists and removes duplicates

# Define a procedure, union,
# that takes as inputs two lists.
# It should modify the first input
# list to be the set union of the two
# lists. You may assume the first list
# is a set, that is, it contains no
# repeated elements.

def union(p, q):
    for e in q:
        if e not in p:
            p.append(e)

# To test, uncomment all lines
# below except those beginning with >>>.

a = [1,2,3]
b = [2,4,6]

union(a,b)
print a
#>>> [1,2,3,4,6]
print b
#>>> [2,4,6]