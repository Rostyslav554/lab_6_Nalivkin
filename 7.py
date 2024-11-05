def is_a_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a


def is_a_right_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return "Неможливо утворити трикутник"
    sides = ([a, b, c])
    sides.sort()
    return sides[2] ** 2 == sides[0] ** 2 + sides[1] ** 2

print(is_a_right_triangle(3, 4, 5))
print(is_a_right_triangle(1, 10, 12))

