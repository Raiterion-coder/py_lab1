n = int(input("Введите четырёхзначное число: "))


chislo1 = n // 1000
chislo2 = (n // 100) % 10
chislo3 = (n // 10) % 10
chislo4 = n % 10

# Найдем минимальную ненулевую цифру
min1 = 10  
if chislo1 > 0:
    min1 = chislo1
if chislo2 > 0 and chislo2 < min1:
    min1 = chislo2
if chislo3 > 0 and chislo3 < min1:
    min1 = chislo3
if chislo4 > 0 and chislo4 < min1:
    min1 = chislo4

#  Уберём min1 из сравнения и сортируем оставшиеся три цифры
if min1 == chislo1:
    x, y, z = chislo2, chislo3, chislo4
elif min1 == chislo2:
    x, y, z = chislo1, chislo3, chislo4
elif min1 == chislo3:
    x, y, z = chislo1, chislo2, chislo4
else:
    x, y, z = chislo1, chislo2, chislo3

# Найдём минимум, средний и максимум
min2 = min(x, y, z)
max2 = max(x, y, z)
mid2 = x + y + z - min2 - max2  # Среднее значение

print(min1 * 1000 + min2 * 100 + mid2 * 10 + max2)
