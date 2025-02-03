summ = 1

while True:
    c1 = int(input("Введите первое число: "))
    oper = input("Введите операцию: ")
    if oper == "x" or oper == "х":
        print(c1)
        break

    elif oper == "!":
        for i in range(1, int(c1) + 1):
            summ *= i
        print(summ)
        continue

    c2 = int(input("Введите второе число: "))

    if oper == "+":
        print(c1 + c2)
    elif oper == "-":
        print(c1 - c2)
    elif oper == "*":
        print(c1 * c2)
    elif oper == "/":
        print(c1 / c2)
    elif oper == "%":
        print(c1 % c2)
    elif oper == "-":
        print(c1 - c2)