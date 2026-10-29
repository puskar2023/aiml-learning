s = {1, 2, 3}

# add element
s.add(6)

# remove element
s.remove(2)
print(s)

# remove a random value
s.pop()

# clear
# s.clear()
print(s)

# Union and Intersection
s1 = {1, 2, 3, 6}
s2 = {1, 6, 5, 9}
print(s1.union(s2))
print(s1.intersection(s2))