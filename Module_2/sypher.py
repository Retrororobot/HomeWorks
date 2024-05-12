number_1 = 3
while 2 < number_1 < 21:
    number_1 = int(
        input("\n\nВведите число первого камня, от 3 до 20. Введите любое другое число, чтобы закончить.\n>"))
    for i in range(1, number_1):
        for j in range(1, number_1):
            if i >= j:
                continue
            if (number_1 % (i + j)) == 0:
                print(f'{i}' + f'{j}', end='')
print("Доктор Джонс гордился бы Вами!")
