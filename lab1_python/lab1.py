import math

def coeff(p):
    while True:
        try:
            coef = float(input(p))
            return coef
        except ValueError:
            print("Некорректное значение.")

a = coeff("Введите коэффициент A: ")
b = coeff("Введите коэффициент B: ")
c = coeff("Введите коэффициент C: ")

if (a==0):
    print("Не является биквадратным уравнением")
    exit()
    
D = b**2 - 4*a*c

if D > 0:
    x1 = (-b + math.sqrt(D)) / (2*a)
    x2 = (-b - math.sqrt(D)) / (2*a)
    print("Уравнение имеет два действительных корня:")
    print("x1 =", x1)
    print("x2 =", x2)
elif D == 0:
    x = -b / (2*a)
    print("Уравнение имеет один действительный корень:")
    print("x =", x)
else:
    print("Уравнение не имеет действительных корней.")
