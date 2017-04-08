def fibonacci_iter(num):
    if num == 0 or num == 1:
        return num
    fib1 = 0
    fib2 = 1
    count = 2
    result = 1
    while count <= num:
        result = fib1 + fib2
        fib1, fib2 = fib2, result
        count += 1
    return result


def fibonacci_rec(num):
    # if num == 0 or num == 1:
    if num <= 2:
        return 1
    return fibonacci_rec(num-1) + fibonacci_rec(num-2)

