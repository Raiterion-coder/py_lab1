login = input("Введите login ")
adress = input("Введите резервный адрес ")
if ("@" not in login):
    print("login введён")
else:
    print("login введен неверно")

if ("@"  in adress):
    print("Резервный адрес введен")
else:
    print("Резервный адрес введен неверно")
