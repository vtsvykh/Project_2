a = float(input())
b = float(input())
c = float(input())
d = b**2 - 4 * a * c < 0
if  a == 0 and b == 0 and c == 0:
    print('Бесконечное количество корней.')
elif d >= 0:
    print(round((-b + d**0.5) / 2 * a, 2), round((-b - d**0.5) / 2 * a, 2))
else:
    if d < 0:
        print('Нет корней.')
