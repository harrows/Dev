def fibonacci(n):
    # Допишите функцию.
    a, b = 0, 1
    for i in range(n):
        yield a
        temp = a 
        a = b 
        b = temp + b


sequence = fibonacci(10)
for number in sequence:
    print(number)