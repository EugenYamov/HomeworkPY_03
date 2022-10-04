numbers_list = [2, 3, 5, 9, 3]
numbers_summ = 0

for index in range(len(numbers_list)):

    if (index % 2) != 0:
        numbers_summ = numbers_summ + numbers_list[index]

print(numbers_summ)