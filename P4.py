import time
def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n-1)
n = 500
# Iterative
start = time.time()
print("Iterative Factorial:", factorial_iterative(n))
end = time.time()
print("Iterative Time:", end - start, "seconds")
# Recursive
start = time.time()
print("Recursive Factorial:", factorial_recursive(n))
end = time.time()
print("Recursive Time:", end - start, "seconds")
