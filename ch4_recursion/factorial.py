#normal solution

def factorial(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num 

print(factorial(7))

# recursive solution
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(7))
