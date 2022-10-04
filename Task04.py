def decimal_to_bin(d):
    bin_number = ''

    while d > 0:
        bin_number = str(d % 2) + bin_number
        d = d // 2

    print (f"\n{bin_number} - ваше число в двоичной системе счисления")

d = int(input('Введите число в десятичной форме: '))

decimal_to_bin(d)