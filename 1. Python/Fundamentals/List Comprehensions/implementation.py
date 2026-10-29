'''
square = []

for i in range(6):
    square.append(i*i)
    
print(square)

sq = [i*i for i in range(6) if i%2 != 0]
print(sq)
'''



'''
nums = [-2, -3, 3, 4, 6, -1, 5]

nums = [0 if val < 0 else val for val in nums]

print(nums)
'''



words = ["hello", "python", "world"]

words = [word.upper() for word in words]

print(words)