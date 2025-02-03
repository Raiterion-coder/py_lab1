n = int(input("Введите n: "))
m = int(input("Введите m: "))
symb = input("Введите символ: ")
print(symb * n)

for i in range(m-2):
    print(symb + (n-2) * " " + symb)

print(symb * n)


