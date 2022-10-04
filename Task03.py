list_numbers = [1.1, 1.2, 3.1, 5, 10.01]
min_item, max_item = 0, 0

for item in list_numbers:

    if item % 1 > max_item:
        max_item = item % 1
    else:
        min_item = item % 1

print (round(max_item - min_item, 2))