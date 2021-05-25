def fibonacci(n):
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    if n == 1:
        value = 1
    if n == 2:
        value = 1
    if n > 2:
        value = fibonacci(n - 1) + fibonacci(n - 2)

#cache update
    fibonacci_cache[n] = value
    return value

#program body
fibonacci_cache = {}

n = int(input())

for i in range (1, n+1):
    print(i,'(digit): ',fibonacci(i))

