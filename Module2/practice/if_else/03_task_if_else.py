# Дан треугольник со сторонами a, b и c. Определите, является ли он равнобедренным.
# Формат входных данных: дано три натуральных числа. Гарантируется, что отрезки с данными длинами образуют треугольник.
# Формат выходных данных: Выведите «YES», если треугольник равнобедренный, и «NO» в противном случае.

# TODO: your code here

a = int(input("First side of triangle ="))
b = int(input("Second side of triangle ="))
c = int(input("Third side of triangle ="))
if a == b or a == c or b==c:
    print ("Yes, the triangle is isosceles")
else:
    print ("No, the triangle isn't isosceles")
