flag = 1
while flag:
    pass1 = input("Введите пароль: ")
    pass2 = input("Введите пароль еще раз: ")
    if (len(pass1) < 8):
        print("Короткий!")
    elif '123' in pass1:
        print("Простой!")
    elif pass1 != pass2:
        print("Различаются.")
    else:
        print("OK")
        flag = 0



