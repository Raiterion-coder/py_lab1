chislo = int(input("Введите целое число: "))
n = 1 # сколько чисел в строке
chislo_v = 1 # переменная для вывода
flag = 0;

while True:

    for k in range(n):
        if chislo_v  == (chislo + 1):
            flag = 1
            break

        print(chislo_v, end=' ')
        chislo_v += 1

    if flag:
        break

    print("")
    n += 1