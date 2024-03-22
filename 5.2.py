xc = int(input())
yc = int(input())
r = int(input())
x = int(input())
y = int(input())


def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2)**(1/2)


def check(xc, yc, r, x, y):
    distanc = distance(xc, yc, x, y)
    if distanc < r:
        return "Точка находится внутри окружности"
    elif distanc == r:
        return "Точка лежит на окружности"
    else:
        return "Точка находится за пределами окружности"


result = check(xc, yc, r, x, y)
print(result)
