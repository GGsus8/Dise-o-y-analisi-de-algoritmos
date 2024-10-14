def fibonacci(n):
    if n < 3:
        return 1
    else:
        return fibonacci(n-2)+fibonacci(n-1)


print(fibonacci(1))  # 1
print(fibonacci(2))  # 1
print(fibonacci(3))  # 3
print(fibonacci(4))  # 13
print(fibonacci(10))  # 55
