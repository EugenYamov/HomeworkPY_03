def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b

n = int(input('Введите число последовательности: ')) + 1
list_fibonacci = list(fibonacci(n))
list_negafibonacci = []

for i in range(len(list_fibonacci)):

    if i % 2 > 0:
        list_negafibonacci.append(list_fibonacci[i] * (-1))
    else:
        list_negafibonacci.append(list_fibonacci[i])

list_negafibonacci.reverse()
print (f'Ваша последовательность: {list_negafibonacci[:-1] + list_fibonacci}')