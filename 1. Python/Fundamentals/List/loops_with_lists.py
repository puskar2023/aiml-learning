list = [1, 6, 9, 3]

x = int(input("Enter the search element: "))
idx = 0

for val in list:
    if (val == x):
        print(f"{x} is present at {idx} index")
        break
    idx += 1