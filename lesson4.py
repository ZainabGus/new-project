print("Введите 1 точку")

x1 = float(input('x: '))

y1 = float(input('y: '))

print("\nВведите 2 точку")

x2 = float(input('x: '))

y2 = float(input('y: '))



x_diff = x1 - x2

y_diff = y1 - y2

k = y_diff / x_diff

b = y2 - k * x2



print("Уравнение прямой, проходящей через эти точки:")

print("y = ", k, " * x + ", b)

