chislo = input("Введите трехзначное число ")
chislo_mas = [chislo[0],chislo[1],chislo[2]]
polusumm = (((int(max(chislo_mas))) + int(min(chislo_mas))) / 2)
chislo_mas.remove(max(chislo_mas))
chislo_mas.remove(min(chislo_mas))
if (polusumm == int(chislo_mas[0])):
    print("Вы ввели красивое число")
else:
    print("Жаль, вы ввели обычное число")