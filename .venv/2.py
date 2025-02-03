str1 = input("Введите первую строку ")
str2 = input("Введите вторую строку ")
if (((str1.lower() == "нет") or (str1.lower() == "да")) and ((str2.lower() == "нет") or (str2.lower() == "да"))):
    print("ВЕРНО")
else:
    print("НЕВЕРНО")