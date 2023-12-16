import math
import unittest

class Tests(unittest.TestCase):

    def test_two_real_roots(self):
        result = equation(1, -3, 2)
        self.assertEqual(result, ("Уравнение имеет два действительных корня:", 2.0, 1.0))

    def test_one_real_root(self):
        result = equation(1, -2, 1)
        self.assertEqual(result, ("Уравнение имеет один действительный корень:", 1))

    def test_no_real_roots(self):
        result = equation(1, 1, 1)
        self.assertEqual(result, "Уравнение не имеет действительных корней.")

def equation(a, b, c):
    if a == 0:
        raise ValueError("Коэффициент A не может быть равен нулю.")
    
    D = b**2 - 4*a*c

    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)
        return ("Уравнение имеет два действительных корня:", x1, x2)
    elif D == 0:
        x = -b / (2*a)
        return ("Уравнение имеет один действительный корень:", x)
    else:
        return "Уравнение не имеет действительных корней."


if __name__ == '__main__':
    unittest.main()
