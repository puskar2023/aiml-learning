# formatting
a = 3
b = 6
sum = a + b

# normal formatting
print("sum of {} and {} is {}".format(a, b, sum))

# index based formatting
print("sum of {1} and {0} is {2}".format(a, b, sum))

# value based formatting
print("sum of {a} and {b} is {sum}".format(a=2, b=3,sum=5))