#factorial

def factorial(n):
    if n is 1:
        return 1
    return n*factorial(n-1)

fac = factorial(6) #6!=720
print("Factorial = ",fac)

#fibonacci
def fibonacci(n):
    if n <= 2:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)
fib = fibonacci(9)
print("Fibonacci = ",fib)
