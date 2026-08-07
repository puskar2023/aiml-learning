def calc_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

N = int(input("Enter the value of N: "))
print((calc_fact(N)))