def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))

def fibonacci(n):
    a, b = 1, 1
    for i in range(n-1):
        a, b = b, a + b
    return a

print(fibonacci(6))

def fibonacci(n):
    prew = cur = 1
    for n in range(n-2):
        tmp = prew + cur
        prew = cur
        cur = tmp
    return cur

print(fibonacci(6))
