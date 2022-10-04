list_numbers = [2, 3, 4, 5, 6]
list_multiplication = []
last_position = len(list_numbers) - 1

for index in range(len(list_numbers)):

    if index <= last_position:
        list_multiplication.append(list_numbers[index] * list_numbers[last_position])
        last_position -= 1

print (list_multiplication)