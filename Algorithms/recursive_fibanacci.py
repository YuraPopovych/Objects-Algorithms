# Let's implement the Fibonacci function we saw in the
# previous video in Python!
#
# Like our Factorial function, our Fibonacci function
# should take as input one parameter, n, an integer. It
# should calculate the nth Fibonacci number. For example,
# fib(7) should give 13 since the 7th number in
# Fibonacci's sequence is 13.

def fib(n):


    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

# Now let's test it out! Run this file to see the results.
print("fib(5) is", fib(5))
print("fib(10) is", fib(10))



