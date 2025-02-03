h = int(input("Введите высоту пирамиды: "))

for i in range(1, int(h) + 1):
    print(" " * (int(h)) + ("*" * ((int(i) * 2) - 1)))
    h -= 1