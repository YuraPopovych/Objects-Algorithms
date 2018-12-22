

def fib3(n):
    if 0 <= n <= 3:
        return 1
    else:
        return fib3(n - 3) + fib3(n - 2) + fib3(n -1)


print(fib3(3))
print(fib3(4))
print(fib3(7))
print(fib3(9))




