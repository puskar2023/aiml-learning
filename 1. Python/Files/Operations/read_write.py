f = open("sample.txt", "r+")

f.write("123")
print(f.read())

f.close()

# Also w+ and a+