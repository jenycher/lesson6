import math

def square(side):
    perimeter = 4 * side
    area = side ** 2
    diagonal = round(math.sqrt(2) * side, 2)
    return perimeter, area, diagonal

# Пример использования функции
side_length = float(input("Введите длину стороны квадрата: "))
perimeter, area, diagonal = square(side_length)
print(f"Периметр квадрата: {perimeter}")
print(f"Площадь квадрата: {area}")
print(f"Диагональ квадрата: {diagonal}")
#В этой функции используется модуль math, чтобы вычислить квадратный корень для определения диагонали квадрата. Функция возвращает кортеж (perimeter, area, diagonal), и затем эти значения распаковываются при вызове функции для вывода каждого из них на экран.






